---
lesson_name: Code execution
layout: layouts/lesson.njk
code_editor: true
code_execution: true
adding_file_allowed: true
hide_content: true
editor_by_output: true
file_groups:
  - common: true
    id: 0
    name: Common files
    files:
      - file_name: text.txt
        file_type: plaintext
        id: 423
        is_closable: true
        is_edit_focus: false
        is_editable: true
        is_hidden: false
        is_main: false
        is_test_file: false
        source: content.txt
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 424
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
  - common: false
    files:
      - file_name: index.js
        file_type: javascript
        id: 425
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: index.js
    id: 2
    name: Javascript
  - common: false
    files:
      - file_name: index.ts
        file_type: typescript
        id: 426
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: index.ts
    id: 4
    name: TypeScript
---

This is a free code execution environment that allows you to run code in the browser. It's a great way to test code snippets and experiment with different programming languages.
