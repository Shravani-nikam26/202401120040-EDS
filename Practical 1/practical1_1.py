#
# Accept mass and velocity as input
mass = float(input())  # Input mass in kilograms
velocity = float(input())  # Input velocity in meters per second

# Calculate momentum
momentum = mass * velocity

# Display the result rounded to 2 decimal places
print(f"{momentum:.2f}kgm/s")
