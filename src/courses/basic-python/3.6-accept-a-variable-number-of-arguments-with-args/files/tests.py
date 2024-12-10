import sys
import re
import json

from inspect import getfullargspec
from unittest.mock import patch

try:
    patched_print = patch('builtins.print')
    patched_print.start()
    import main
    patched_print.stop()
    
except Exception:
    pass

results = {}

try:
    assert callable(main.accept_all)
    results[1] = True
except Exception:
    results[1] = False

try:
    argspec = getfullargspec(main.accept_all)
    assert argspec.varargs is not None
    results[2] = True
except Exception:
    results[2] = False

sys.stdout.write(json.dumps(results))