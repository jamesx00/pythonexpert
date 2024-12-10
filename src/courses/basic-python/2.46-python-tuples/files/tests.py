import sys
import re
import json

from unittest.mock import patch
patch('builtins.print').start()

try:
    import main
except Exception:
    pass

try:
    assert type(main.numbers) == tuple
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))