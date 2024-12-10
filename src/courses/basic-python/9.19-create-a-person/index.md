---
lesson_name: Create a Person
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 443
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 444
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

### Create a person

Create a `Person` class to have properties and methods satisfying all the tests.

---

### Tests

<ul>
<li id="test-1">A <code>Person</code> object is created with the code <code>person = Person("samson craig", 30, "male", "software engineer")</code><ul>
<li id="test-2"><code>person.first_name</code> should be <code>"Samson"</code>. Make sure the case is right.</li>
<li id="test-3"><code>person.last_name</code> should be <code>"Craig"</code>. Make sure the case is right.</li>
<li id="test-4"><code>person.age</code> should be <code>30</code></li>
<li id="test-5"><code>person.occupation</code> should be <code>"software engineer"</code></li>
<li id="test-6"><code>person.introduce()</code> should print the message <code>"Hello, my name is Samson. I am 30 years old. I am a male working as a software engineer."</code></li>
<li id="test-7"><code>person.celebrate_birthday()</code> should increase the <code>age</code> property by <code>1</code></li>
<li id="test-8"><code>person.introduce()</code> should print the message <code>"Hello, my name is Samson. I am 31 years old. I am a male working as a software engineer."</code> after <code>person.celebrate_birthday()</code></li>
<li id="test-9"><code>person.change_job("data analyst")</code> should set the <code>occupation</code> property to <code>"data analyst"</code></li>
<li id="test-10"><code>person.introduce()</code> should print the message <code>"Hello, my name is Samson. I am 31 years old. I am a male working as a data analyst."</code> after <code>person.celebrate_birthday()</code></li>
</ul>
</li>
</ul>
