def factorial(num):
    result = 1 # Start with 1 (the base case for factorial)
    for i in range(1, (num + 1)): # Loop from 1 to num (inclusive)
        result *= i # Multiply result by the current number
    return result # Final calculated factorial