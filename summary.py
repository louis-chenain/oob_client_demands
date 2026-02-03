# ==========================================
# FINANCIAL SUMMARY - EDUCATIONAL VERSION
# ==========================================
# This script "pulls it all together".
# It reads both Invoices and Expenses to calculate the Net Profit.
# Students: Observe how we reuse the file-reading pattern here!

INVOICE_DATA = "invoices.txt"
EXPENSE_DATA = "expenses.txt"

def sum_csv_column(filename, column_index):
    """Sums the values in a specific column of a CSV file, skipping the header.
    Handles file not found and invalid numbers gracefully."""
    total = 0.0
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        for line in lines[1:]:  # Skip header
            parts = line.strip().split(",")
            if len(parts) > column_index:
                try:
                    total += float(parts[column_index])
                except ValueError:
                    print(f"Warning: Invalid number in {filename}: '{parts[column_index]}' - skipping this line.")
    except FileNotFoundError:
        print(f"[!] No file found: {filename}. Total is $0.")
    return total

# Initialize our totals
income_total = 0.0
expense_total = 0.0

# --- 1. PROCESS INCOMES (INVOICES) ---
print("Reading Invoice data...")
income_total = sum_csv_column(INVOICE_DATA, 2)

# --- 2. PROCESS OUTGOINGS (EXPENSES) ---
print("Reading Expense data...")
expense_total = sum_csv_column(EXPENSE_DATA, 2)

# --- 3. FINAL CALCULATION ---
profit_or_loss = income_total - expense_total

# --- 4. DISPLAY THE REPORT ---
print("\n" + "="*35)
print("      YEAR-TO-DATE SUMMARY")
print("="*35)
print(f"Total Gross Income:   ${income_total:10.2f}")
print(f"Total Business Costs: ${expense_total:10.2f}")
print("-" * 35)

if profit_or_loss >= 0:
    print(f"NET PROFIT:          +${profit_or_loss:10.2f}")
else:
    print(f"NET LOSS:            -${abs(profit_or_loss):10.2f}")

print("="*35 + "\n")
print("TIPS for Students:")
print("- Could you make a function that sums a specific CSV column?")
print("- How would you handle errors if a file is corrupted?")
