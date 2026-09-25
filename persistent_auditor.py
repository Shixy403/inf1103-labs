# ==============================================================================
# INF1103 Lab 4: Data Persistence
# File: persistent_auditor.py
# Phase a: After load_inventory() is added
# ==============================================================================

def get_valid_input():
    str_input = input("Type 'quit' to exit. Enter stock quantity: ").strip()

    if str_input.lower() == "quit":
        return "quit"

    if str_input.isdigit():
        return int(str_input)
    else:
        if str_input.startswith("-"):
            print("Error: Negative numbers are not allowed.")
        else:
            print("Error: Invalid entry. Please enter whole numbers only.")
        return ""


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts, deliveries_processed):
    print("\n--- Final Audit Report ---")
    print("Total Deliveries Processed:", deliveries_processed)
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)


def load_inventory(filename):
    """
    Reads existing total inventory from disk.
    If the file does not exist, it creates a new file initialized with 0.
    """
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()
        
        if not lines:
            return 0
        
        return int(lines[0])

    except FileNotFoundError:
        # File is missing, so create a new one immediately
        with open(filename, "w") as file:
            file.write("0\n")
        
        print(f"'{filename}' not found. Created a new file initialized with 0.")
        return 0


def main():
    print("=== Smart Inventory Auditor Initialized (Persistent) ===")

    # Load inventory from file instead of starting hardcoded at 0
    inventory = load_inventory("inventory.txt")
    failed_entries = 0
    deliveries_processed = 0

    print("Current starting inventory:", inventory)

    while True:
        entry = get_valid_input()

        if entry == "quit":
            break
        elif entry == "":
            failed_entries = failed_entries + 1
        else:
            tax = calculate_tax(entry)
            inventory = process_delivery(inventory, entry)
            deliveries_processed = deliveries_processed + 1

            print("Accepted:", entry, "units. Current total:", inventory, "Tax:", tax)

    generate_report(inventory, failed_entries, deliveries_processed)


if __name__ == "__main__":
    main()