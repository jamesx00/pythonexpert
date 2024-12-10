import sys
import re
import json
import inspect

from unittest.mock import patch

results = {}

with patch('builtins.print') as patched_print:

    try:
        import main
    except Exception as e:
        pass

    try:
        assert main.D().method() == "C"
        results[1] = True
    except Exception as e:
        results[1] = False
    
    try:
        no_implementation_change = (
            main.A().method() == "A" 
            and main.B().method() == "B"
            and main.C().method() == "C"
            and "method" not in main.D.__dict__
        )

        assert no_implementation_change
        results[2] = True
    except Exception as e:
        results[2] = False
    
    try:
        inherit_from_all_classes = (
            issubclass(main.D, main.A)
            and issubclass(main.D, main.B)
            and issubclass(main.D, main.C)
        )
        assert inherit_from_all_classes
        results[3] = True
    except Exception as e:
        results[3] = False

sys.stdout.write(json.dumps(results))