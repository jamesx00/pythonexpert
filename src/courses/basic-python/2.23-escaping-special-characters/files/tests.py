import sys
import re

from unittest.mock import patch
patch('builtins.print').start()

try:
    import main
except Exception:
    pass

import json

try:
    assert main.file_path == r"C:\Users\John\Documents"
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))