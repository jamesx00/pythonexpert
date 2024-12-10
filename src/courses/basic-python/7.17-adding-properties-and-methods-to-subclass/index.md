---
lesson_name: Adding Properties and Methods to Subclass
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 370
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 371
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Adding properties and methods to subclass

If we define new methods or assign new properties in a subclass, those methods and properties will be accessible only in the objects created from that subclass and not the parent. This allows you to extend and customize the functionality of the parent class according to the specific needs of the subclass.

For example:

```python
class Parent:
    def __init__(self):
        self.parent_property = "Parent Property"

class Child(Parent):
    def __init__(self):
        self.parent_property = "Parent Property"
        self.child_property = "Child Property"

    def child_method(self):
        print("This is called from a Child object")

parent = Parent()
child = Child()
print(parent.parent_property)  # Output: Parent Property
print(child.parent_property)  # Output: Parent Property
print(child.child_property)   # Output: Child Property

print(parent.child_property) # AttributeError: 'Parent' object has no attribute 'child_property'
```

In the example above, both the `Parent` and `Child` classes have their own `parent_property` property, but only the child class has a `child_property` property. When we try to access `child_property` in a `Parent` object, we get an error <span class="text-red-500">AttributeError: 'Parent' object has no attribute 'child_property'</span>.

The same is true for methods as well. When we try and call the `child_method` from a `Parent` object, we get an error <span class="text-red-500">AttributeError: 'Parent' object has no attribute 'child_method'</span>.

```python
child.child_method() # This is called from a Child object
parent.child_method() # AttributeError: 'Parent' object has no attribute 'child_method'
```

---

### Exercise

- Add the property `grade` and method `study` to the `Student` class.

#### Tests

<ul>
<li id="test-1"><code>Person</code> objects should <strong>not</strong> have the property <code>grade</code></li>
<li id="test-2"><code>Person</code> objects should <strong>not</strong> have the method <code>study</code></li>
<li id="test-3"><code>Student</code> objects should have the property <code>grade</code></li>
<li id="test-4"><code>Student</code> objects should have the method <code>study</code></li>
<li id="test-5">The object created from <code>Student("Liam", 13, 7)</code> should have the following properties<ul>
<li id="test-6"><code>grade</code> should be <code>7</code></li>
<li id="test-7"><code>study()</code> method should print out the message <code>"Liam is a student"</code></li>
</ul>
</li>
</ul>
