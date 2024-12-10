import sys
import json

from unittest.mock import patch

sys.stdout.write(json.dumps({1: True}))