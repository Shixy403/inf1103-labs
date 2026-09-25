# ==============================================================================
# INF1103 Lab 4: Data Persistence
# File: persistent_auditor.py
# Phase b: After tracking history list
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


def generate_report(total_units, failed_attempts, history):
    print("\n--- Final Audit Report ---")
    print("Total Deliveries Processed:", len(history))
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Transaction History (List):", history)


def load_inventory(filename):
    """
    Reads existing total and transaction history from disk.
    If file is missing, creates it with 0 and returns an empty list.
    """
    try:
        with open(filename, "r") as file:
            lines = file.read().splitlines()

        if not lines:
            return 0, []

        total = int(lines[0])
        history = []
        for line in lines[1:]:
            # we skips index 0 / total 
            # start:end - leaving blank, means to start from index 1 all the way to the end
            history.append(int(line))

        return total, history

    except FileNotFoundError:
        # Create a new file initialized with 0
        with open(filename, "w") as file:
            file.write("0\n")

        print(f"'{filename}' not found. Created a new file initialized with 0.")
        return 0, []


def main():
    print("=== Smart Inventory Auditor Initialized (Persistent) ===")

    # Load starting total and history list
    inventory, history = load_inventory("inventory.txt")
    failed_entries = 0

    print("Current starting inventory:", inventory)
    print("Existing history:", history)

    while True:
        entry = get_valid_input()

        if entry == "quit":
            break
        elif entry == "":
            failed_entries = failed_entries + 1
        else:
            tax = calculate_tax(entry)
            inventory = process_delivery(inventory, entry)
            
            # Record every valid transaction amount in the list
            history.append(entry)

            print("Accepted:", entry, "units. Current total:", inventory, "Tax:", tax)

    # Display final report including the tracked history list
    generate_report(inventory, failed_entries, history)


if __name__ == "__main__":
    main()