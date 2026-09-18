import json
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'records.json')

def load_data():
    """Loads records from the JSON file. Returns an empty list if file doesn't exist or is empty."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: Data file is corrupted. Starting with an empty record list.")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def save_data(records):
    """Saves the current list of records to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as file:
            json.dump(records, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

def get_valid_input(prompt, validation_type="text"):
    """Helper function to get validated input from the user."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be empty. Please try again.")
            continue
            
        if validation_type == "text":
            return value
        elif validation_type == "age":
            try:
                age = int(value)
                if 18 <= age <= 100:
                    return age
                else:
                    print("Please enter a valid age between 18 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number for age.")
        elif validation_type == "email":
            if re.match(r"[^@]+@[^@]+\.[^@]+", value):
                return value
            else:
                print("Invalid email format. Please try again.")
        elif validation_type == "phone":
            if re.match(r"^\d{10,15}$", value):
                return value
            else:
                print("Invalid phone number. Please enter 10-15 digits only.")

def generate_id(records):
    """Generates a unique ID for a new record based on the highest existing ID."""
    if not records:
        return 1
    try:
        max_id = max(int(record['id']) for record in records)
        return max_id + 1
    except ValueError:
        return len(records) + 1
    except KeyError:
        return len(records) + 1

def add_record(records):
    """Adds a new employee record after validating input."""
    print("\n--- Add New Employee Record ---")
    name = get_valid_input("Enter Name: ", "text")
    age = get_valid_input("Enter Age (18-100): ", "age")
    department = get_valid_input("Enter Department: ", "text")
    email = get_valid_input("Enter Email: ", "email")
    phone = get_valid_input("Enter Phone Number: ", "phone")

    new_id = generate_id(records)
    new_record = {
        'id': new_id,
        'name': name,
        'age': age,
        'department': department,
        'email': email,
        'phone': phone
    }
    records.append(new_record)
    save_data(records)
    print(f"\nSuccess! Record for '{name}' added with ID: {new_id}")

def print_record_table(records):
    """Helper function to print a list of records in a tabular format."""
    if not records:
        print("No records found.")
        return
        
    print("-" * 105)
    print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Department':<15} | {'Email':<25} | {'Phone':<15}")
    print("-" * 105)
    for record in records:
        print(f"{record['id']:<5} | {record['name']:<20} | {record['age']:<5} | {record['department']:<15} | {record['email']:<25} | {record['phone']:<15}")
    print("-" * 105)

def view_records(records):
    """Displays all existing records."""
    print("\n--- View All Records ---")
    if not records:
        print("No records exist yet in the database.")
    else:
        print_record_table(records)

def search_record(records):
    """Searches for records by ID or Name (partial match)."""
    print("\n--- Search Records ---")
    search_term = input("Enter ID or Name to search: ").strip().lower()
    
    if not search_term:
        print("Search term cannot be empty.")
        return

    results = []
    for record in records:
        # Match exactly by ID or partially by Name
        if str(record['id']) == search_term or search_term in record['name'].lower():
            results.append(record)
            
    if results:
        print(f"\nFound {len(results)} matching record(s):")
        print_record_table(results)
    else:
        print(f"\nNo records found matching '{search_term}'.")

def update_record(records):
    """Locates a record by ID and allows the user to modify its fields."""
    print("\n--- Update Record ---")
    try:
        record_id = int(input("Enter the ID of the record to update: ").strip())
    except ValueError:
        print("Invalid ID format. Please enter a valid number.")
        return

    # Find the record
    target_record = None
    for record in records:
        if record['id'] == record_id:
            target_record = record
            break
            
    if not target_record:
        print(f"Record with ID {record_id} not found.")
        return

    print("\nCurrent Record Details:")
    print_record_table([target_record])
    
    print("\nEnter new values (leave blank to keep current value):")
    
    name_input = input(f"Name [{target_record['name']}]: ").strip()
    if name_input:
        target_record['name'] = name_input
        
    while True:
        age_input = input(f"Age [{target_record['age']}]: ").strip()
        if not age_input:
            break
        try:
            age = int(age_input)
            if 18 <= age <= 100:
                target_record['age'] = age
                break
            else:
                print("Age must be between 18 and 100.")
        except ValueError:
            print("Invalid input. Age must be a number.")

    dep_input = input(f"Department [{target_record['department']}]: ").strip()
    if dep_input:
        target_record['department'] = dep_input
        
    while True:
        email_input = input(f"Email [{target_record['email']}]: ").strip()
        if not email_input:
            break
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_input):
            target_record['email'] = email_input
            break
        else:
            print("Invalid email format.")
            
    while True:
        phone_input = input(f"Phone [{target_record['phone']}]: ").strip()
        if not phone_input:
            break
        if re.match(r"^\d{10,15}$", phone_input):
            target_record['phone'] = phone_input
            break
        else:
            print("Invalid phone format. Enter 10-15 digits.")

    save_data(records)
    print("\nRecord updated successfully!")

def delete_record(records):
    """Locates a record by ID and removes it after confirmation."""
    print("\n--- Delete Record ---")
    try:
        record_id = int(input("Enter the ID of the record to delete: ").strip())
    except ValueError:
        print("Invalid ID format. Please enter a valid number.")
        return

    # Find index of the record
    target_index = -1
    for i, record in enumerate(records):
        if record['id'] == record_id:
            target_index = i
            break
            
    if target_index == -1:
        print(f"Record with ID {record_id} not found.")
        return

    print("\nRecord to be deleted:")
    print_record_table([records[target_index]])
    
    confirm = input("Are you sure you want to delete this record? (y/n): ").strip().lower()
    if confirm == 'y':
        deleted_record = records.pop(target_index)
        save_data(records)
        print(f"\nRecord for '{deleted_record['name']}' deleted successfully.")
    else:
        print("\nDeletion cancelled.")

def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*35)
    print("  EMPLOYEE RECORD MANAGEMENT SYSTEM  ")
    print("="*35)
    print("1. Add Record")
    print("2. View All Records")
    print("3. Search Record")
    print("4. Update Record")
    print("5. Delete Record")
    print("6. Exit")
    print("="*35)

def main():
    """Main execution loop of the application."""
    print("Starting application...")
    records = load_data()
    print(f"Loaded {len(records)} record(s) from database.")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            add_record(records)
        elif choice == '2':
            view_records(records)
        elif choice == '3':
            search_record(records)
        elif choice == '4':
            update_record(records)
        elif choice == '5':
            delete_record(records)
        elif choice == '6':
            print("\nExiting Employee Record Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
