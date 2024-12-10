import sys
import json

from unittest.mock import patch
patch('builtins.print').start()

import main

try:
    assert main.x == 10, "Assign x with the number 10: Failed X"
    sys.stdout.write(json.dumps({1: True}))
except Exception as e:
    sys.stdout.write(json.dumps({1: False}))