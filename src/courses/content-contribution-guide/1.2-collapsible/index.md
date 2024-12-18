---
lesson_name: Collapsible
code_editor: True
code_execution: False
adding_file_allowed: False
file_groups:
  - common: false
    files:
    - file_name: content.md
      file_type: auto-detect
      id: 473
      is_closable: false
      is_edit_focus: true
      is_editable: true
      is_hidden: false
      is_main: true
      is_test_file: false
      source: content.md
    id: 1
    name: Markdown
  
---
### Collapsible content

```markdown
#### With content hidden

<details><summary>Toggle me!</summary>Peek a boo!</details>

#### With content showing

<details open>
<summary>Shopping list</summary>

* Vegetables
* Fruits
* Fish
</details>
```

#### With content hidden

<details><summary>Toggle me!</summary>Peek a boo!</details>

#### With content showing

<details open>
<summary>Solution</summary>
<pre><code class="hljs language-python"><span class="hljs-built_in">print</span>(<span class="hljs-string">"This is amazing!"</span>)
</code></pre>
</details>


#### With content showing

<details open>
<summary></summary>

* Vegetables
* Fruits
* Fish
</details>