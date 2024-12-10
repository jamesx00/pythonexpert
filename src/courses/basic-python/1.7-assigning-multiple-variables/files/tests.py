import sys
from unittest.mock import patch
import json

patch('builtins.print').start()



try:
    import main
except Exception:
    pass

with open('main.py', 'r') as file:
    results = {}

    file_content = file.readlines()

    try:
        assert main.x == 10
        assert main.y == 20
        assert main.z == 30
        results[1] = True
    except Exception as e:
        results[1] = False

    try:
        assert len(file_content) == 1
        results[2] = True
    except Exception as e:
        results[2] = False

    sys.stdout.write(json.dumps(results))