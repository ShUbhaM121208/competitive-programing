def chewbacca_and_number(x):
    # Convert number to string
    x = str(x)
    result = []

    for i, digit in enumerate(x):
        digit = int(digit)
        inverted = 9 - digit

        # Choose the smaller value, except for leading zero case
        if i == 0 and inverted == 0:  # Handle leading zero case
            result.append(str(digit))
        else:
            result.append(str(min(digit, inverted)))

    # Join the result into a string and return
    return ''.join(result)

# Input
x = int(input("Enter the number: "))
# Output
print(chewbacca_and_number(x))
