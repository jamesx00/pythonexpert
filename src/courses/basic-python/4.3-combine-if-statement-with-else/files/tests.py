import sys
import re
import json

from unittest.mock import patch

try:
    patched_print = patch('builtins.print')
    patched_print.start()
    import main
    patched_print.stop()
    
except Exception:
    pass

longer_sentence = "That is longer than 5 characters."
shorter_sentence = "That is not longer than 5 characters."

results = {}

with patch('main.print') as p_print:

    try:
        main.is_longer_than_5_characters("1234")
        p_print.assert_called_once_with(shorter_sentence)
        results[1] = True
    except Exception as e:
        results[1] = False

with patch('main.print') as p_print:

    try:
        main.is_longer_than_5_characters("12345")
        p_print.assert_called_once_with(shorter_sentence)
        results[2] = True
    except Exception as e:
        results[2] = False

with patch('main.print') as p_print:

    try:
        main.is_longer_than_5_characters("123456")
        p_print.assert_called_once_with(longer_sentence)
        results[3] = True
    except Exception as e:
        results[3] = False


sys.stdout.write(json.dumps(results))