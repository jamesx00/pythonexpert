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

def test_find_second_largest(numbers):
    # Easier method
    # copy_numbers = numbers.copy()
    # copy_numbers.sort(reverse=True)
    # return copy_numbers[1]

    largest_number = None
    second_largest_number = None
    
    for num in numbers:
        if largest_number is None:
            largest_number = num
            continue
        
        if second_largest_number is None:
            if num > largest_number:
                second_largest_number = largest_number
                largest_number = num
            else:
                second_largest_number = num
            continue

        if num > largest_number:
            second_largest_number = largest_number
            largest_number = num
        elif num > second_largest_number:
            second_largest_number = num

    return second_largest_number
    

inputs = [
    ([1, 3, 5, 7, 9],),
    ([10, 5, 8, 2, 6],), 
    ([9, 9, 9, 9, 9],),
    ([15, 10, 20, 5, 25],),
    ([-5, -10, -3, -8, -1],),
]

results = {}

for index, i in enumerate(inputs):
    try:
        result = test_find_second_largest(*i)
        assert main.find_second_largest(*i) == result
        results[index + 1] = True
    except Exception as e:
        print(e)
        results[index + 1] = False

sys.stdout.write(json.dumps(results))