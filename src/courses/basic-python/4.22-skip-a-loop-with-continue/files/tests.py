import sys
import re
import json

from unittest.mock import patch, call


with patch('builtins.print') as patched_print:

    try:
        import main
    except Exception:
        pass

    try:
        patched_print.assert_has_calls([call(0), call(2), call(4), call(6), call(8)])
        sys.stdout.write(json.dumps({1: True}))
    except Exception as e:
        sys.stdout.write(json.dumps({1: False}))