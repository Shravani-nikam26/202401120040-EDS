# Accept an integer input for the number of rows
n = int(input())

# Loop to print the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # Move to the next line after each row
