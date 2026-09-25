# assignment


A simple and friendly employee management system built in Python. It helps you add, view, search, update, and delete employee records from a terminal menu while saving everything locally in a JSON file.

## Features
- Add new employees with validation
- View all stored records in a neat table
- Search by employee ID or name
- Update existing records
- Delete records with confirmation
- Automatically save data to `records.json`

## How to run
```bash
python main.py
```

## Example records table
| ID | Name | Age | Department | Email | Phone |
| --- | --- | --- | --- | --- | --- |
| 1 | Jane Doe | 29 | Sales | jane@example.com | 0987654321 |
| 2 | Alex Martin | 34 | Engineering | alex.martin@company.com | 9876543210 |
| 3 | Priya Nair | 27 | HR | priya.nair@company.com | 9123456780 |
| 4 | Daniel James | 41 | Finance | daniel.james@company.com | 9988776655 |

## Sample console output
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
Enter your choice (1-6): 2

--- View All Records ---
ID    | Name          | Age | Department | Email                    | Phone
1     | Jane Doe      | 29  | Sales      | jane@example.com         | 0987654321
2     | Alex Martin   | 34  | Engineering | alex.martin@company.com | 9876543210
3     | Priya Nair    | 27  | HR         | priya.nair@company.com  | 9123456780
4     | Daniel James  | 41  | Finance    | daniel.james@company.com | 9988776655
```

## Project structure
- `main.py` — application logic
- `records.json` — employee storage
- `README.md` — project documentation

## Notes
This project is lightweight, beginner-friendly, and useful for understanding basic CRUD operations in Python.
