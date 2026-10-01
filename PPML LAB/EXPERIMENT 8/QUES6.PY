import numpy as np
harvest_data = np.array([
    [50, 55, 60, 52, 58, 65, 70],       # Tomatoes
    [30, 32, 28, 35, 33, 40, 42],       # Carrots
    [100, 95, 105, 110, 98, 120, 125],  # Potatoes
    [40, 38, 42, 45, 91, 50, 55]        # Onions
])

# PART 1: ARRAY PROPERTIES AND RESTRUCTURING

print("Shape:", harvest_data.shape)
print("Number of dimensions:", harvest_data.ndim)
print("Total size:", harvest_data.size)

day_crop_data = harvest_data.T

print("\nRestructured Array (Days x Crops):")
print(day_crop_data)


# PART 2: STATISTICAL OPERATIONS

# 3. Weekly crop yield
weekly_yield = np.sum(harvest_data, axis=1)

print("\nWeekly Yield of Each Crop:")
print("Tomatoes:", weekly_yield[0], "kg")
print("Carrots:", weekly_yield[1], "kg")
print("Potatoes:", weekly_yield[2], "kg")
print("Onions:", weekly_yield[3], "kg")

# 4. Daily average across all crops
daily_average = np.mean(harvest_data, axis=0)

print("\nDaily Average Yield:")
print(daily_average)

# 5. Best day / maximum single-crop yield
best_yield = np.max(harvest_data)

print("\nMaximum Single-Crop Yield:", best_yield, "kg")

# PART 3: BROADCASTING
# 6. Fertilizer bonus
bonus = 10
fertilizer_bonus = np.array([0, 0, 0, 0, bonus, bonus, bonus])
bonus_data = harvest_data + fertilizer_bonus
print("\nAfter Fertilizer Bonus:")
print(bonus_data)


# CROP SHRINKAGE - ADVANCED BROADCASTING
shrinkage = np.array([0.95, 0.98, 0.99, 0.97])
shrinkage = shrinkage.reshape(4, 1)
final_weight = bonus_data * shrinkage
print("\nFinal Transported Weight:")
print(final_weight)
