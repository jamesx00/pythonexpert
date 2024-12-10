import sys
import re
import json

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

try:
    import main
except Exception:
    pass

conversion_unit = 1.609

results = {}

try:
    result = 0 / conversion_unit
    assert main.convert_km_to_mi(0) == result
    results[1] = True
except Exception:
    results[1] = False


try:
    result = 10 / conversion_unit
    assert main.convert_km_to_mi(10) == result
    results[2] = True
except Exception:
    results[2] = False

try:
    result = 20 / conversion_unit
    assert main.convert_km_to_mi(20) == result
    results[3] = True
except Exception:
    results[3] = False

sys.stdout.write(json.dumps(results))