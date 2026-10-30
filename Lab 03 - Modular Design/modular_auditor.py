# ==============================================================================
# inf1103 lab 3: modular design
# file: modular_auditor.py
# ==============================================================================

# get_valid_input() > returns int or quit string
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


def main():
    print("=== Smart Inventory Auditor Initialized (Modular) ===")

    inventory = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
        entry = get_valid_input()

        if entry == "quit":
            break
        elif entry == "":
            failed_entries = failed_entries + 1
        else:
            # tabulate inventory, delivery_count and tax
            tax = calculate_tax(entry)
            inventory = process_delivery(inventory, entry)
            deliveries_processed = deliveries_processed + 1

            print("Accepted:", entry, "units. Current total:", inventory, "Tax:", tax)

    generate_report(inventory, failed_entries, deliveries_processed)


if __name__ == "__main__":
    main()