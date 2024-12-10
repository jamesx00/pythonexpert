import sys
import re
import json

from unittest.mock import patch

with patch('builtins.print') as patched_print:

    try:
        import main
    except Exception:
        pass

    try:
        assert len(patched_print.call_args_list) == 5
        file_content = open('main.py', 'r').read()
        assert re.search('while', file_content) is not None
        sys.stdout.write(json.dumps({1: True}))
    except Exception as e:
        sys.stdout.write(json.dumps({1: False}))