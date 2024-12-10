---
lesson_name: Get Last Watch time
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 435
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 436
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

### Get last watch time

Given a dictionary of users and their watching history, write a function that retrieves the last watch time for a specific user and video. If the user hasn't watched the video, return `0`. If the user doesn't exist, return `None`.

---

### Tests

<ul>
<li id="test-0">Do not change the given dictionary</li>
<li id="test-1"><code>get_last_watch_time("user1@email.com", "A Journey into the Quantum Banana")</code> should return <code>15</code></li>
<li id="test-2"><code>get_last_watch_time("user2@email.com", "A Journey into the Quantum Banana")</code> should return <code>30</code></li>
<li id="test-3"><code>get_last_watch_time("user2@email.com", "Cats in Space and Intergalactic Cheese")</code> should return <code>5</code></li>
<li id="test-4"><code>get_last_watch_time("user3@email.com", "Cats in Space and Intergalactic Cheese")</code> should return <code>0</code></li>
<li id="test-5"><code>get_last_watch_time("user1@email.com", "Time-Traveling Penguins and Singing Tacos")</code> should return <code>0</code></li>
<li id="test-6"><code>get_last_watch_time("user999@email.com", "Time-Traveling Penguins and Singing Tacos")</code> should return <code>None</code></li>
</ul>
