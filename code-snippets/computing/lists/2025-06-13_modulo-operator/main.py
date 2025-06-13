def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0: # An odd number when divided by 2, the remainder is not 0
            odd_numbers.append(i) # Adds it to list of odd numbers

    # don't touch below this line

    return odd_numbers
