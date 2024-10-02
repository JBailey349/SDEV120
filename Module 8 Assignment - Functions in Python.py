def greaterThan(x, y):
    # Check if x is greater than y
    if x > y:
        return True
    else:
        return False

# Main section of the program
a = 10
b = 6

# Call the function and store the result
result = greaterThan(a, b)

# Print the output
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(result) + ".")
