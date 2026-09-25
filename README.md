# Employee Record Management System

A simple **console-based Employee Record Management System** developed using Python.
This project demonstrates fundamental Python programming concepts including functions, loops, conditional statements, exception handling, and JSON file handling.

## 📌 Project Description

The Employee Record Management System allows users to manage employee information through a menu-driven console application.

The application supports:

* Adding employee records
* Viewing all employee records
* Searching for an employee
* Updating employee information
* Deleting employee records
* Storing records permanently in a JSON file

## 🛠️ Technologies Used

* **Python 3**
* **JSON** – for storing employee records
* **OS module** – for file and directory handling
* **Regular Expressions (`re`)** – for input validation

## 📚 Python Concepts Demonstrated

### 1. Data Types and Variables

The project uses different Python data types:

* `String` – Name, Department, Email, Phone
* `Integer` – ID and Age
* `List` – Collection of employee records
* `Dictionary` – Individual employee record
* `Boolean` – Used in conditional logic

Example:

```python
new_record = {
    'id': new_id,
    'name': name,
    'age': age,
    'department': department,
    'email': email,
    'phone': phone
}
```

### 2. Conditional Statements and Loops

The project uses:

* `if`
* `elif`
* `else`
* `for` loops
* `while` loops

These are used for menu selection, searching records, validating input, and keeping the application running until the user chooses to exit.

### 3. Functions

The application is divided into multiple functions to make the program organized and reusable.

Main functions include:

```text
load_data()
save_data()
get_valid_input()
generate_id()
add_record()
view_records()
search_record()
update_record()
delete_record()
display_menu()
main()
```

### 4. Exception Handling

`try-except` blocks are used to prevent the program from crashing because of invalid input or file errors.

Example:

```python
try:
    age = int(value)
except ValueError:
    print("Invalid input. Please enter a number for age.")
```

### 5. File I/O

Employee records are stored in a file named:

```text
records.json
```

The project uses:

```python
json.load()
```

to read existing records and:

```python
json.dump()
```

to save records.

This allows employee data to remain available even after the program is closed.

### 6. Menu-Driven Console Application

The application provides the following menu:

```text
===================================
  EMPLOYEE RECORD MANAGEMENT SYSTEM
===================================
1. Add Record
2. View All Records
3. Search Record
4. Update Record
5. Delete Record
6. Exit
===================================
```

## ✨ Features

### Add Record

Allows the user to enter:

* Name
* Age
* Department
* Email
* Phone Number

A unique ID is automatically generated for every new employee.

### View All Records

Displays all stored employee records in a table.

### Search Record

Allows the user to search by:

* Employee ID
* Employee Name

### Update Record

Allows existing employee information to be modified using the employee ID.

### Delete Record

Allows the user to delete an employee record after confirmation.

## 🔐 Input Validation

The application validates user input before storing it.

* Age must be between **18 and 100**
* Phone number must contain **10–15 digits**
* Email must follow a basic email format
* Empty inputs are not accepted where validation is required

## 📁 Project Structure

```text
Employee-Record-Management-System/
│
├── main.py
├── records.json
└── README.md
```

> Replace `main.py` with the actual name of your Python file if you have given it a different name.

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed on your computer.

### Step 2: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### Step 3: Open the Project Folder

```bash
cd Employee-Record-Management-System
```

### Step 4: Run the Program

```bash
python main.py
```

### Step 5: Select an Option

Enter a number from **1 to 6** according to the operation you want to perform.

## 💾 Data Storage

The application uses `records.json` as its local database.

Example:

```json
[
    {
        "id": 1,
        "name": "Rahul",
        "age": 25,
        "department": "IT",
        "email": "rahul@example.com",
        "phone": "9876543210"
    }
]
```

## 🔄 CRUD Operations

| Operation | Function            |
| --------- | ------------------- |
| Create    | Add Record          |
| Read      | View/Search Records |
| Update    | Update Record       |
| Delete    | Delete Record       |

## 🎯 Project Objective

The main objective of this project is to demonstrate the practical implementation of fundamental Python programming concepts by developing a functional console-based Employee Record Management System.

## 👩‍💻 Author

**Sneha Sujeesh**

MCA Semester I
Python Programming & Relational Database
