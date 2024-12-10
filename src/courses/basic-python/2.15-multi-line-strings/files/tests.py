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
    assert type(main.address) == str
    assert re.search('\n', main.address) is not None
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))