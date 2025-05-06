import math 

# Accepting input from the user
num = int(input())

# Check the number of digits in the input
if 1 <= num <= 9:  # Single-digit number
    print(num ** 2)
elif 10 <= num <= 99:  # Two-digit number
    print(f"{math.sqrt(num):.2f}")
elif 100 <= num <= 999:  # Three-digit number
    print(f"{math.pow(num, 1/3):.2f}")
else:  # If number is out of the given range
    print("Invalid")
