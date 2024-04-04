# This program loads a dataset of life expectancies and finds the lowest and highest values.
# Additionally, it calculates and displays the average life expectancy.

lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')
total_life_expectancy = 0
count = 0

with open('life.csv', 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        life_expectancy = float(parts[3])
        total_life_expectancy += life_expectancy
        count += 1
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

average_life_expectancy = total_life_expectancy / count

print(f"The lowest life expectancy is: {lowest_life_expectancy}")
print(f"The highest life expectancy is: {highest_life_expectancy}")
print(f"The average life expectancy is: {average_life_expectancy:.2f}")
