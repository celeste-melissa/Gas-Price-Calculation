mileage = float(input("Enter your car's gas mileage range:"))
cost_per_gallon = float(input("Enter the cost of gas per gallon:"))

# Distance for 20 miles
distance_20 = 20
price_distance_20 = (distance_20 / mileage) * cost_per_gallon

# Distance for 75 miles
distance_75 = 75
price_distance_75 = (distance_75 / mileage) * cost_per_gallon

# Distance for 500 miles
distance_500 = 500
price_distance_500 = (distance_500 / mileage) * cost_per_gallon

# Calculated gas prices
print(f"Cost of gas for 20 miles: {price_distance_20:.3f}")
print(f"Cost of gas for 75 miles: {price_distance_75:.2f}")
print(f"Cost of gas for 500 miles: {price_distance_500:.2f}")
