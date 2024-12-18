---
lesson_name: What is a Database
code_editor: False
code_execution: False
adding_file_allowed: False
---

## What is a database

![](https://asset.pythonexpert.dev/media/markdownx/2024/05/09/261196c9-716a-4723-9c9b-32b24899d461.jpg)

A database is a structured collection of data organized for efficientstorage, retrieval, and management. It serves as a centralized repository where information can be stored, updated, and accessed by various applications and users.

## What is relational database

A relational database is a type of database that uses a structure based on tables and the relationships between them. It follows the principles of the relational model, where data is organized into tables with rows and columns, and relationships between tables are defined.

### Example of popular relational databases

- MySQL: An open-source relational database management system (RDBMS).
  Used in various applications, from small-scale websites to large enterprise systems.

- PostgreSQL: An open-source object-relational database system.
  Known for its extensibility and support for complex queries.

- Microsoft SQL Server: A relational database management system developed by Microsoft.
  Widely used in enterprise environments for data storage and retrieval.

- Oracle Database: A multi-model relational database management system.
  Often used in large-scale enterprise applications.

- SQLite: A zero-configuration relational database engine. Suitable for embedded systems, mobile applications, and small to medium-sized websites.

With multiple options to choose from, one good thing about SQL is that how you write a command in an option could be very similar or even the same in another. We will be working with SQLite in this course, and will build our own PostgreSQL server with Amazon AWS.

### Data relationships

Data relationships are a fundamental aspect of how information is organized and interconnected in various domains. And almost everything in the world exhibits data relationships. Consider a company managing customer and order information:

- **Customers Table:**

  | CustomerID | FirstName | LastName | Email            |
  | ---------- | --------- | -------- | ---------------- |
  | 1          | John      | Doe      | john@example.com |
  | 2          | Jane      | Smith    | jane@example.com |
  | 3          | Bob       | Johnson  | bob@example.com  |

- **Orders Table:**

  | OrderID | CustomerID | Product    | Quantity | OrderDate  |
  | ------- | ---------- | ---------- | -------- | ---------- |
  | 101     | 1          | Laptop     | 2        | 2023-02-15 |
  | 102     | 2          | Smartphone | 1        | 2023-02-16 |
  | 103     | 3          | Headphones | 3        | 2023-02-17 |

In this example, there are two tables: `Customers` and `Orders`. The `CustomerID` in the `Orders` table establishes a relationship with the `Customers` table, connecting orders to specific customers. We will cover data relationships further in the course.
