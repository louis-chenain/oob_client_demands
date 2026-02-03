# ==========================================
# CLIENT MANAGEMENT - EDUCATIONAL VERSION !
# ==========================================
# This script manages client data in a text file.
# Students: Notice how the code is grouped into logical sections.
# Each section could eventually become a function!

# --- 1. INITIALIZATION ---
FILENAME = "clients.txt"

def init_db(filename=FILENAME):
    try:
        with open(filename, "r", encoding="utf-8"):
            pass
        return False
    except FileNotFoundError:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("id,name,email\n")
        return True

# --- 2. MAIN MENU LOOP (MENU BLOCK) ---
def menu_block():
    print("\n" + "="*25)
    print("   CLIENT MANAGEMENT")
    print("="*25)
    print("1. Add a New Client")
    print("2. View All Clients")
    print("3. Exit Program")
    print("-" * 25)

    user_choice = input("What would you like to do? ")
    return user_choice

# --- 3. ADD CLIENT SECTION ---
def add_client_block():
    print("\nAdding a new client...")
    name = input("- Name: ")
    email = input("- Email: ")
    
    # Step: Calculate the next ID (number of lines in file)
    db_read = open(FILENAME, "r")
    all_lines = db_read.readlines()
    db_read.close()
    new_id = len(all_lines)
    
    # Step: Append the new client to the file
    db_append = open(FILENAME, "a")
    # Format: id,name,email
    db_append.write(str(new_id) + "," + name + "," + email + "\n")
    db_append.close()
    
    print(f"DONE! Client '{name}' saved with ID {new_id}.")

# --- 4. LIST CLIENTS SECTION ---
def list_clients_block():
    print("\n" + "-"*30)
    print("      CURRENT CLIENT LIST")
    print("-"*30)
    
    db_view = open(FILENAME, "r")
    header = db_view.readline() # Skip the first line (header)
    
    current_line = db_view.readline()
    while current_line:
        # Step: Parse the line into pieces
        # Students: .split(',') turns "1,John,mail" into ["1", "John", "mail"]
        data_parts = current_line.strip().split(",")
        
        if len(data_parts) >= 3:
            client_id = data_parts[0]
            client_name = data_parts[1]
            client_email = data_parts[2]
            print(f"ID: {client_id} | Name: {client_name} | Email: {client_email}")
        
        current_line = db_view.readline()
        
    db_view.close()
    print("-" * 30)

# --- 5. EXIT SECTION ---
def exit_block():
    print("Goodbye!")
created = init_db()
print("DB created?", created)

#easy use of def 
while True:
    user_choice = menu_block()

    if user_choice == '1':
        add_client_block()

    elif user_choice == '2':
        list_clients_block()

    elif user_choice == '3':
        exit_block()
        break

    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
