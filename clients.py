# ==========================================
# CLIENT MANAGEMENT - EDUCATIONAL VERSION !
# ==========================================
# This script manages client data in a text file.
# Students: Notice how the code is grouped into logical sections.
# Each section could eventually become a function!

FILENAME = "clients.txt"

# --- 1. INITIALIZATION ---
# Check if the file exists, if not, create it with a header.
try:
    file_check = open(FILENAME, "r")
    file_check.close()
except FileNotFoundError:
    print("Initializing database...")
    database = open(FILENAME, "w")
    database.write("id,name,email\n")
    database.close()

# --- 2. MAIN MENU LOOP ---
while True:
    print("\n" + "="*25)
    print("   CLIENT MANAGEMENT")
    print("="*25)
    print("1. Add a New Client")
    print("2. View All Clients")
    print("3. Exit Program")
    print("-" * 25)
    
    user_choice = input("What would you like to do? ")

    # --- 3. ADD CLIENT SECTION ---
    if user_choice == '1':
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
    elif user_choice == '2':
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
    elif user_choice == '3':
        print("Goodbye!")
        break
        
    else:
        print("Invalid choice. Please pick 1, 2, or 3.")
