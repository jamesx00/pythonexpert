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

little_spicy = "A little spicy"
very_spicy = "Very spicy"
not_spicy = "Not spicy"

results = {}

try:
    assert main.get_spicy_message(3) == not_spicy
    results[1] = True
except Exception as e:
    results[1] = False

try:
    assert main.get_spicy_message(4) == little_spicy
    results[2] = True
except Exception as e:
    results[2] = False

try:
    assert main.get_spicy_message(5) == very_spicy
    results[3] = True
except Exception as e:
    results[3] = False

try:
    assert main.get_spicy_message(6) == very_spicy
    results[4] = True
except Exception as e:
    results[4] = False

sys.stdout.write(json.dumps(results))