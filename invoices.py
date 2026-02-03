import os
from typing import List, Optional, Callable, Dict

FILENAME: str = "invoices.txt"
HEADER: str = "id,client_id,amount,date,description\n"

# --- 1. DATA ACCESS ---

def read_lines(filename: str) -> List[str]:
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(HEADER)
        return [HEADER]
    with open(filename, "r") as f:
        return f.readlines()

def append_line(filename: str, data_row: str) -> None:
    with open(filename, "a") as f:
        f.write(data_row)

# --- 2. PURE LOGIC ---

def format_invoice_string(invoice_id: int, details: List[str]) -> str:
    """Uses type hints to ensure we receive an int and a list of strings."""
    return f"{invoice_id},{','.join(details)}\n"

def parse_invoice_line(line: str) -> Optional[str]:
    """Returns a string if valid, or None if the line is corrupt/header."""
    parts = line.strip().split(",")
    if len(parts) < 5 or parts[0] == "id": 
        return None
    return f"INV #{parts[0]} | Client {parts[1]} | ${parts[2]} | {parts[3]} | {parts[4]}"

# --- 3. RECURSIVE INTERFACE ---

def main_menu() -> None:
    """The main interface, now driven by recursion instead of a while loop."""
    
    print(f"\n{'!'*25}\n   INVOICE TRACKER\n{'!'*25}")
    print("1. Create New Invoice\n2. List All Invoices\n3. Exit")
    
    choice: str = input("Selection: ")

    # Define the dispatch table with type hinting for the values
    actions: Dict[str, Callable[[], None]] = {
        '1': handle_create,
        '2': handle_list,
        '3': lambda: print("Exiting...")
    }

    # Execute selection
    if choice in actions:
        actions[choice]()
        # RECURSION: If not exiting, call main_menu again to "loop"
        if choice != '3':
            main_menu()
    else:
        print("Invalid Selection.")
        main_menu()

# --- 4. ACTION HANDLERS ---

def handle_create() -> None:
    inputs: List[str] = [
        input("- Client ID: "),
        input("- Amount: "),
        input("- Date (YYYY-MM-DD): "),
        input("- Description: ")
    ]
    new_id: int = len(read_lines(FILENAME))
    append_line(FILENAME, format_invoice_string(new_id, inputs))
    print(f"Invoice #{new_id} saved.")

def handle_list() -> None:
    print("\n--- INVOICE HISTORY ---")
    lines: List[str] = read_lines(FILENAME)
    # Using map/filter for a declarative data pipeline
    display_items = filter(None, map(parse_invoice_line, lines))
    
    # We use a simple for-loop here for printing (I/O side effect)
    for item in display_items:
        print(item)

if __name__ == "__main__":
    main_menu()