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

    name = "Liam"
    age = 13
    grade = 7

    person = main.Person(name, age)
    student = main.Student(name, age, grade)
    
    try:
        assert hasattr(person, "grade") == False
        results[1] = True
    except Exception as e:
        results[1] = False
    
    try:
        assert hasattr(person, "study") == False
        results[2] = True
    except Exception as e:
        results[2] = False

    try:
        assert hasattr(student, "grade")
        results[3] = True
    except Exception as e:
        results[3] = False
    
    try:
        assert hasattr(student, "study")
        results[4] = True
    except Exception as e:
        results[4] = False
    
    try:
        assert hasattr(student, "grade")
        results[3] = True
    except Exception as e:
        results[3] = False
    
    try:
        assert student.grade == grade
        results[6] = True
    except Exception as e:
        results[6] = False
    
    try:
        student.study()
        patched_print.assert_called_with(f"{name} is a student")
        results[7] = True
    except Exception as e:
        results[7] = False

    results[5] = results[6] and results[7]

sys.stdout.write(json.dumps(results))