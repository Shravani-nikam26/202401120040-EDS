# Accept the input as an integer
num = int(input())

# Reverse the digits by converting the number to a string, reversing it, and converting it back to an integer
reversed_num = int(str(num)[::-1])

# Output the reversed number
print(reversed_num)
