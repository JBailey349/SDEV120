import csv

# Sample data for Gerald's Businesses
geralds_data = [
    ['4891', 'Smith', 'South Bend', '1500'],
    ['4978', 'Miller', 'Bloomington', '9800'],
    ['5144', 'Johnson', 'Terre Haute', '3500'],
    ['8949', 'Garcia', 'Fort Wayne', '2500'],
    ['9841', 'Brown', 'Gary', '3000'],
]

# Sample data for Geraldine's Businesses
geraldines_data = [
    ['4891', 'Smith', 'South Bend', '1500'],
    ['1598', 'Jones', 'Jeffersonville', '1500'],
    ['2578', 'Smith', 'Evansville', '2500'],
    ['6548', 'Robertson', 'Indianapolis', '1000'],
    ['9853', 'Erickson', 'Clarksville', '1750'],
    ['9856', 'Jacobs', 'Columbus', '1900'],
]

# Function to create CSV files
def create_csv(filename, data):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Create the CSV files
create_csv('Geralds_Businesses.csv', geralds_data)
create_csv('Geraldines_Businesses.csv', geraldines_data)

print("CSV files created successfully!")

def merge_customer_records(geralds_file, geraldines_file, output_file):
    # Declare a set to keep track of unique customer numbers
    unique_customers = set()
    merged_records = []

    # Open and read Gerald's Businesses
    with open(geralds_file, mode='r', newline='') as geralds:
        reader = csv.reader(geralds)
        for row in reader:
            customer_number = row[0]  # Get unique customer number
            if customer_number not in unique_customers:
                unique_customers.add(customer_number)
                merged_records.append(row)  # Append the record to merged records

    # Open and read Geraldine's Businesses
    with open(geraldines_file, mode='r', newline='') as geraldines:
        reader = csv.reader(geraldines)
        for row in reader:
            customer_number = row[0]  # Get unique customer number
            if customer_number not in unique_customers:
                unique_customers.add(customer_number)
                merged_records.append(row)  # Append the record to merged records

    # Write merged records to the output file
    with open(output_file, mode='w', newline='') as output:
        writer = csv.writer(output)
        writer.writerows(merged_records)  # Write all merged records to the output file

# Sample file names
geralds_file = 'Geralds_Businesses.csv'
geraldines_file = 'Geraldines_Businesses.csv'
output_file = 'Merged_Customers.csv'

# Call the merge function
merge_customer_records(geralds_file, geraldines_file, output_file)

print("Customer records merged successfully!")

