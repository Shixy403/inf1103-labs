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

