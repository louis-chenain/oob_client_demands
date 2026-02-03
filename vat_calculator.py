# ==========================================
# VAT CALCULATOR - EDUCATIONAL VERSION
# ==========================================
# A simple tool to calculate "Value Added Tax".
# This uses basic arithmetic: (amount * rate) / 100

print("\n" + "*"*25)
print("   TAX CALCULATOR")
print("*"*25)

# --- 1. USER INPUT ---
def init():
    raw_amount = input("Enter the net amount (e.g. 100): ")
    raw_rate = input("Enter the VAT rate % (press Enter for 20%): ")
    return raw_amount, raw_rate

# --- 2. LOGIC AND CALCULATION ---
# We use a try/except block to catch people entering text instead of numbers!
def log_calc(raw_amount, raw_rate):
    try:
    # Step A: Convert inputs to decimal numbers (floats)
        net_value = float(raw_amount)
    
    # Step B: Default to 20.0 if the user just pressed Enter
        if raw_rate == "":
            tax_rate = 20.0
        else:
            tax_rate = float(raw_rate)
    
    # Step C: The Math
        tax_to_pay = net_value * (tax_rate / 100.0)
        total_price = net_value + tax_to_pay
    
    # --- 3. DISPLAY RESULTS ---
        print("\nCALCULATION SUMMARY:")
        print(f"- Net Amount:   ${net_value:.2f}")
        print(f"- VAT ({tax_rate}%): ${tax_to_pay:.2f}")
        print("-" * 25)
        print(f"- TOTAL PRICE:  ${total_price:.2f}")
        print("*" * 25 + "\n")

    except ValueError:
    # This runs if float() failed!
        print("\n[!] ERROR: Please enter digits only (e.g. 12.50).")
raw_amount, raw_rate = init()
log_calc(raw_amount, raw_rate)
