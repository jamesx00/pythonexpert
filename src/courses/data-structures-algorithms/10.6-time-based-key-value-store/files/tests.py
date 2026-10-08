import sys
import json
import bisect

from unittest.mock import patch
patch('builtins.print').start()

import main

def test_func(ops):
    store = {}
    results = []
    for op in ops:
        if op[0] == "set":
            _, key, value, timestamp = op
            store.setdefault(key, []).append((timestamp, value))
        else:
            _, key, timestamp = op
            entries = store.get(key, [])
            i = bisect.bisect_right(entries, (timestamp, chr(0x10FFFF)))
            results.append(entries[i - 1][1] if i > 0 else "")
    return results

def run_main(ops):
    tm = main.TimeMap()
    results = []
    for op in ops:
        if op[0] == "set":
            _, key, value, timestamp = op
            tm.set(key, value, timestamp)
        else:
            _, key, timestamp = op
            results.append(tm.get(key, timestamp))
    return results

inputs = [
    ([("set", "temp", "72F", 1), ("get", "temp", 1)],),
    ([("set", "temp", "72F", 1), ("set", "temp", "75F", 4), ("get", "temp", 2)],),
    ([("set", "temp", "72F", 1), ("set", "temp", "75F", 4), ("get", "temp", 4)],),
    ([("set", "temp", "72F", 1), ("set", "temp", "75F", 4), ("get", "temp", 10)],),
    ([("set", "temp", "72F", 1), ("set", "temp", "75F", 4), ("get", "temp", 0)],),
    ([("get", "missing", 5)],),
    ([("set", "a", "1", 1), ("set", "a", "2", 2), ("set", "a", "3", 3), ("get", "a", 3), ("get", "a", 2)],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert run_main(*i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
