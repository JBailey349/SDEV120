def calculate_bill(text_messages):
    BASE_FEE = 5
    FIRST_100_LIMIT = 100
    SECOND_LIMIT = 300
    OVER_300_RATE = 0.02  # 2 cents
    BETWEEN_100_300_RATE = 0.03  # 3 cents
    TAX_RATE = 0.14
    
    total_cost = BASE_FEE

    if text_messages > FIRST_100_LIMIT:
        total_cost += (min(text_messages, SECOND_LIMIT) - FIRST_100_LIMIT) * BETWEEN_100_300_RATE

    if text_messages > SECOND_LIMIT:
        total_cost += (text_messages - SECOND_LIMIT) * OVER_300_RATE

    total_tax = total_cost * TAX_RATE
    total_bill = total_cost + total_tax

    return total_bill

def main():
    customers = []  # Store customer data

    while True:
        # Collect input data
        area_code = input("Enter area code (3 digits): ")
        phone_number = input("Enter phone number (7 digits): ")
        text_messages = int(input("Enter total number of text messages sent (or -1 to quit): "))

        # Check for sentinel value
        if text_messages == -1:
            break

        # Display input data
        print(f"Area Code: {area_code}")
        print(f"Phone Number: {phone_number}")
        print(f"Text Messages Sent: {text_messages}")

        # Calculate and display the monthly bill
        monthly_bill = calculate_bill(text_messages)
        print(f"Monthly Bill (including taxes): ${monthly_bill:.2f}")

        # Store customer data based on conditions
        if text_messages > 100:
            customers.append({"area_code": area_code, "phone_number": phone_number, "text_messages": text_messages, "bill": monthly_bill})

    # Display customers who sent over 100 messages
    print("\nCustomers who sent over 100 messages:")
    for customer in customers:
        print(customer)

    # Check for bills exceeding $10
    print("\nCustomers with a bill exceeding $10:")
    for customer in customers:
        if customer['bill'] > 10:
            print(customer)

    # Area code specific functionality
    search_area_code = input("\nEnter area code to view specific bills: ")
    print(f"\nBills from area code {search_area_code}:")
    for customer in customers:
        if customer['area_code'] == search_area_code:
            print(customer)

if __name__ == "__main__":
    main()
