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