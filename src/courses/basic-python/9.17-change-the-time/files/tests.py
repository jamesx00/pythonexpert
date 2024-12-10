import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

def test_func(current_time, minutes):
    hours, mins = map(int, current_time.split(':'))
    
    total_minutes = hours * 60 + mins
    updated_minutes = total_minutes + minutes

    updated_hours = (updated_minutes // 60) % 24
    updated_mins = updated_minutes % 60

    updated_time = "{:02d}:{:02d}".format(updated_hours, updated_mins)

    return updated_time
    
inputs = [
    ("12:30", 45,),
    ("23:45", -90,),
    ("06:00", 120,),
    ("09:15", -60,),
    ("18:30", 0,),
    ("23:55", 10,),
    ("00:05", -10,),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.change_time(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))