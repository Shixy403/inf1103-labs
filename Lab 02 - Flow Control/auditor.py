# ==============================================================================
# INF1103 Lab 2: Smart Inventory Auditor
# File: auditor.py
# ==============================================================================

# Requirement 1: Initialize the inventory to zero at the start.
# We also initialize a counter to track invalid/rejected user inputs.
inventory = 0
failed_entries = 0

print("=== Smart Inventory Auditor Initialized ===")

# Requirement 2: Run in a continuous loop until the user types 'quit'
while True:
    # Use .strip() to remove accidental spaces around the input
    user_input = input("Type 'quit' to exit. Enter stock quantity: ").strip()
    
    # Requirement 2: Check for exit condition
    if user_input.lower() == "quit":
        break       # exits loop and goes to audit report printing.


    # Requirement 3 & 4: Process positive integer values
    if user_input.isdigit():
        # Requirement 3: Convert string input to integer
        quantity = int(user_input)

        # Requirement 6: Manage State - Keep running total
        inventory = inventory + quantity
        print("Accepted:", quantity, "units. Current total:", inventory)

        # Requirement 7: Trigger Overstock Alert (> 500 units)
        if inventory > 500:
            print("ALERT: Overstock limit exceeded (> 500)! Halting process.")
            break

    # Requirement 4 & 5: Handle invalid inputs
    else:
        if user_input.startswith("-"):
            print("Error: Negative numbers are not allowed.")
        else:
            print("Error: Invalid entry. Please enter whole numbers only.")
        
        failed_entries = failed_entries + 1

# Requirement 8: Final Audit Reporting
print("\n--- Final Audit Report ---")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)