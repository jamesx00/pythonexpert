import sys
import re
import json
import math

from unittest.mock import patch

patched_print = patch('builtins.print')
patched_print.start()

history = {
    "user1@email.com": {
        "A Journey into the Quantum Banana": 15
    },
    "user2@email.com": {
        "A Journey into the Quantum Banana": 30,
        "Cats in Space and Intergalactic Cheese": 5
    },
    "user3@email.com": {
        "Time-Traveling Penguins and Singing Tacos": 10
    },
}

try:
    import main
except Exception:
    pass

def test_func(user, video):
    if user not in history:
        return None
    return history[user].get(video, 0)
    
inputs = [
    ("user1@email.com", "A Journey into the Quantum Banana",),
    ("user2@email.com", "A Journey into the Quantum Banana", ),
    ("user2@email.com", "Cats in Space and Intergalactic Cheese", ),
    ("user3@email.com", "Cats in Space and Intergalactic Cheese", ),
    ("user1@email.com", "Time-Traveling Penguins and Singing Tacos", ),
    ("user999@email.com", "Time-Traveling Penguins and Singing Tacos", ),
]

results = {}

try:
    assert main.history == history
    results[0] = True
except Exception as e:
    results[0] = False

for index, i in enumerate(inputs):
    try:
        result = test_func(*i)
        assert main.get_last_watch_time(*i) == result
        results[index + 1] = True
    except Exception as e:
        results[index + 1] = False

sys.stdout.write(json.dumps(results))