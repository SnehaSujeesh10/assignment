# Assignment Report: Console Record-Management Application

## 1. Design Approach
The application is designed as a standalone, menu-driven console program with a strong focus on modularity, data integrity, and error prevention. By isolating the data structure (a list of dictionaries) and abstracting the file operations, the program effectively separates concerns. The chosen entity is an "Employee" with six structured fields: ID, Name, Age, Department, Email, and Phone. JSON was selected as the storage format because of its excellent mapping to Python dictionaries and lists, which makes the persistence layer both robust and human-readable.

## 2. Module Breakdown
The application logic is contained within `main.py`, structured into distinct, single-responsibility functions:
- `load_data()` / `save_data()`: Handles all File I/O.
- `get_valid_input()`: A reusable helper that uses Regex and try-except blocks to enforce validation logic.
- `generate_id()`: Dynamically calculates the next available ID.
- `add_record()`, `view_records()`, `search_record()`, `update_record()`, `delete_record()`: Implement the core CRUD functionalities.
- `print_record_table()`: A dedicated helper for formatting output text consistently.
- `display_menu()` / `main()`: Controls the program flow and execution loop.

## 3. Explicit Implementation of Python Concepts

### Data Types & Variables
- **Integers**: Used for mathematical and comparison operations on IDs and Age.
- **Strings**: Used for string manipulations, partial matching in searches (via `.lower()`), and textual data storage (Name, Department).
- **Lists & Dictionaries**: A List of Dictionaries represents the entire in-memory database. Each dictionary maps string keys to corresponding values (e.g., `{'id': 1, 'name': 'John Doe', ...}`).

### Conditional Statements & Loops
- **Menu Routing (`if/elif/else`)**: Implemented in `main()` to map user numeric choices to the corresponding function executions.
- **Iteration (`for`)**: Used in `search_record()`, `update_record()`, and `delete_record()` to traverse the list of dictionaries and locate specific records.
- **Indefinite Loops (`while`)**: Used in `main()` for the continuous application run loop and in `get_valid_input()` to repeatedly ask the user until valid input is provided.

### Functions (Modularity)
Instead of a monolithic script, functionality is encapsulated. Data is passed between functions (e.g., passing the `records` list to `add_record(records)`) minimizing reliance on global state (aside from the constant `DATA_FILE` path). 

### Exception Handling
- **Input Resilience**: The `try/except ValueError` pattern is explicitly utilized in `get_valid_input()` and numerical prompts (e.g., in `update_record()` and `delete_record()`) to intercept and handle `ValueError` when a user inputs text instead of integers.
- **File I/O Safety**: `load_data()` uses a `try/except` block to capture `json.JSONDecodeError` ensuring the program doesn't crash if `records.json` gets corrupted. It acts gracefully by returning an empty list instead.

### File I/O
The built-in `json` module is used for data persistence. `load_data()` runs at application startup, initializing the in-memory array. The `save_data()` function takes the `records` list and writes it completely to `records.json` using `json.dump()`. This save operation is immediately invoked after any modifying function (`add_record`, `update_record`, `delete_record`) keeping the disk representation synchronized without memory-disk lag.
