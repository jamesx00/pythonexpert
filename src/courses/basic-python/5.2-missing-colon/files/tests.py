import sys
import re
import json

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    try:
        import main
        main.can_you_vote(18)
        patched_print.assert_called_with('You are eligible to vote.')
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        import main
        main.can_you_vote(15)
        patched_print.assert_called_with('You are not eligible to vote.')
        results[2] = True
    except Exception as e:
        results[2] = False

sys.stdout.write(json.dumps(results))