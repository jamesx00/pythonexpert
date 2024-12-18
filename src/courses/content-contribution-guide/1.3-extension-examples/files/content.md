# Keys

++ctrl+alt+delete++

# Emoji

:smile: :heart: :thumbsup:

# Details

/// details | Some summary
attrs: {class: border border-red-500 px-3 cursor-pointer mb-4}
type: warning

Some content
///

#### Opening as default

/// details | Some summary
attrs: {class: border border-red-500 px-3 cursor-pointer mb-4}
open: True
type: warning

Something
///

# Alerts

<div class="alert-info">
This is the content

```python
print("OKAY")
```

</div>

<div class="alert-warning">
This is the content

```python
print("OKAY")
```

</div>

<div class="alert-danger">
This is the content

```python
print("OKAY")
```

</div>

# Code blocks {.mt-4}

Paragraph.

```
a fenced block
```

Another paragraph.

> ```
>   a fenced block
> ```

> with blank lines

````
### Code blocks inside list

- &#32;
  ```
  a fenced block
  ```

Definition
: &#32;
  ```
  a fenced block
  ```

### Code block with line numbers

#### With class


# Mermaid

```mermaid
pie title NETFLIX
       "Time spent looking for movie" : 90
       "Time spent watching it" : 10
````

```mermaid
sequenceDiagram
    participant web as Web Browser
    participant blog as Blog Service
    participant account as Account Service
    participant mail as Mail Service
    participant db as Storage

    Note over web,db: The user must be logged in to submit blog posts
    web->>+account: Logs in using credentials
    account->>db: Query stored accounts
    db->>account: Respond with query result

    alt Credentials not found
        account->>web: Invalid credentials
    else Credentials found
        account->>-web: Successfully logged in

        Note over web,db: When the user is authenticated, they can now submit new posts
        web->>+blog: Submit new post
        blog->>db: Store post data

        par Notifications
            blog--)mail: Send mail to blog subscribers
            blog--)db: Store in-site notifications
        and Response
            blog-->>-web: Successfully posted
        end
    end
```
