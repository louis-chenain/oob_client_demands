import os
from typing import List, Optional, Callable, Dict

FILENAME: str = "expenses.txt"
HEADER: str = "id,category,amount,date,description\n"

# --- 1. DATA ACCESS LAYER (Impure/IO) ---

def get_db_lines(filename: str) -> List[str]:
    """Reads all lines, initializing the file if it doesn't exist."""
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(HEADER)
        return [HEADER]
    with open(filename, "r") as f:
        return f.readlines()

def save_entry(filename: str, csv_line: str) -> None:
    """Appends a new line to the persistent storage."""
    with open(filename, "a") as f:
        f.write(csv_line)

# --- 2. TRANSFORMATION LAYER (Pure Functions) ---

def create_csv_string(entry_id: int, fields: List[str]) -> str:
    """Combines an ID and list of inputs into a single CSV line."""
    return f"{entry_id},{','.join(fields)}\n"

def format_for_display(line: str) -> Optional[str]:
    """Transforms a raw CSV line into a formatted table row."""
    parts = line.strip().split(",")
    if len(parts) < 5 or parts[0] == "id":
        return None
    
    eid, cat, val, dt, ds = parts
    return f"ID {eid:2} | {dt} | {cat:10} | ${val:>7} | {ds}"

# --- 3. ACTION HANDLERS ---

def record_expense() -> None:
    print("\nEntering expense data:")
    user_inputs = [
        input("- Category: "),
        input("- Amount: "),
        input("- Date (YYYY-MM-DD): "),
        input("- Description: ")
    ]
    
    # Calculate ID based on existing data
    current_data = get_db_lines(FILENAME)
    new_id = len(current_data)
    
    # Transform and Save
    csv_data = create_csv_string(new_id, user_inputs)
    save_entry(FILENAME, csv_data)
    print(f"SAVED: '{user_inputs[0]}' expense recorded.")

def view_expenses() -> None:
    print("\n--- RECORDED EXPENSES ---")
    raw_lines = get_db_lines(FILENAME)
    
    # Functional pipeline: Filter out header/errors, then format each line
    display_rows = filter(None, map(format_for_display, raw_lines))
    
    for row in display_rows:
        print(row)
    print("-" * 30)

# --- 4. THE RECURSIVE INTERFACE ---

def run_tracker() -> None:
    """Replaces the 'while' loop with a recursive call."""
    print(f"\n{'-'*30}\n      EXPENSE TRACKER\n{'-'*30}")
    print("1. Record a New Expense\n2. View All Expenses\n3. Exit")
    
    choice = input("Option: ")

    # Dispatch Table (Functions as first-class objects)
    menu_actions: Dict[str, Callable[[], None]] = {
        '1': record_expense,
        '2': view_expenses,
        '3': lambda: print("Closing Expense Tracker...")
    }

    action = menu_actions.get(choice)

    if action:
        action()
        # Recursion: Call self again unless exiting
        if choice != '3':
            run_tracker()
    else:
        print("Error: Input 1, 2, or 3.")
        run_tracker()

if __name__ == "__main__":
    run_tracker()