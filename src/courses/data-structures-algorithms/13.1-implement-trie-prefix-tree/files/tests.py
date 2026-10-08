import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main


class RefTrie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = RefTrie()
            node = node.children[ch]
        node.is_word = True

    def search(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_word

    def starts_with(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


def run_ops(trie, ops):
    results = []
    for method, args in ops:
        ret = getattr(trie, method)(*args)
        results.append(ret)
    return results


def test_func(ops):
    return run_ops(RefTrie(), ops)


inputs = [
    ([("insert", ("cat",)), ("search", ("cat",))],),
    ([("insert", ("cat",)), ("search", ("ca",)), ("starts_with", ("ca",))],),
    ([("insert", ("bat",)), ("insert", ("bath",)), ("search", ("bat",)),
      ("search", ("bath",)), ("search", ("ba",))],),
    ([("starts_with", ("z",))],),
    ([("insert", ("apple",)), ("insert", ("app",)), ("search", ("app",)),
      ("starts_with", ("appl",)), ("search", ("appl",))],),
    ([("insert", ("wolf",)), ("insert", ("wolf",)), ("search", ("wolf",)),
      ("starts_with", ("wo",))],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert run_ops(main.Trie(), *i) == result
        results[index + 1] = True
    except Exception:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))
