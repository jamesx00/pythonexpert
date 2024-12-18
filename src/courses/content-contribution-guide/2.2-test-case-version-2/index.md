---
lesson_name: Test case version 2
code_editor: True
code_execution: True
adding_file_allowed: True
file_groups:
  - common: false
    files:
    - file_name: tests.py
      file_type: python
      id: 315
      is_closable: false
      is_edit_focus: false
      is_editable: false
      is_hidden: true
      is_main: false
      is_test_file: true
      source: tests.py
    - file_name: main.py
      file_type: python
      id: 314
      is_closable: false
      is_edit_focus: true
      is_editable: true
      is_hidden: false
      is_main: true
      is_test_file: false
      source: main.py
    id: 1
    name: Python
  
---
#### Test case version 2

To implement test cases version 2, each test case is a list item with an integer as an id.

For example, this is the code that populates the test cases in this lesson:

```html
<ul>
<li id="test-1"><code>convert_to_title("hello world!")</code> should return <code>"Hello World!"</code>.</li>
<li id="test-2"><code>convert_to_title("the cat in the hat.")</code> should return <code>"The Cat In The Hat."</code>.</li>
<li id="test-3"><code>convert_to_title("i love coding.")</code> should return <code>"I Love Coding."</code>.</li>
<li id="test-4"><code>convert_to_title("this is a test sentence.")</code> should return <code>"This Is A Test Sentence."</code>.</li>
<li id="test-5"><code>convert_to_title("the quick brown fox.")</code> should return <code>"The Quick Brown Fox."</code>.</li>
</ul>
```

Which generates below list

<ul>
<li id="test-1"><code>convert_to_title("hello world!")</code> should return <code>"Hello World!"</code>.</li>
<li id="test-2"><code>convert_to_title("the cat in the hat.")</code> should return <code>"The Cat In The Hat."</code>.</li>
<li id="test-3"><code>convert_to_title("i love coding.")</code> should return <code>"I Love Coding."</code>.</li>
<li id="test-4"><code>convert_to_title("this is a test sentence.")</code> should return <code>"This Is A Test Sentence."</code>.</li>
<li id="test-5"><code>convert_to_title("the quick brown fox.")</code> should return <code>"The Quick Brown Fox."</code>.</li>
</ul>

To implement a test script, in the main file group, create a file with the value "is test file" checked. The script should write a JSON oject to the output with the indexes being the number of the test id, and the value being boolean type as the test result. For example:

```json
{
    1: true,
    2: false,
}
```

To see the test file for this lesson, see the file `test.py` in the code editor.