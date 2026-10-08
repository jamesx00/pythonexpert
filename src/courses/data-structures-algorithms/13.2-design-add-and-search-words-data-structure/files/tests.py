import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main


class RefWordDictionary:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def add_word(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = RefWordDictionary()
            node = node.children[ch]
        node.is_word = True

    def search(self, pattern):
        def dfs(node, i):
            if i == len(pattern):
                return node.is_word
            ch = pattern[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self, 0)


def run_ops(wd, ops):
    results = []
    for method, args in ops:
        ret = getattr(wd, method)(*args)
        results.append(ret)
    return results


def test_func(ops):
    return run_ops(RefWordDictionary(), ops)


inputs = [
    ([("add_word", ("dog",)), ("search", ("dog",))],),
    ([("add_word", ("dog",)), ("search", ("cat",))],),
    ([("add_word", ("dog",)), ("search", (".og",))],),
    ([("add_word", ("dog",)), ("search", ("d.g",)), ("search", ("do.",))],),
    ([("add_word", ("bear",)), ("add_word", ("beat",)), ("search", ("bea.",)),
      ("search", ("bean",))],),
    ([("add_word", ("a",)), ("search", (".",)), ("search", ("..",))],),
    ([("search", ("...",))],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert run_ops(main.WordDictionary(), *i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
