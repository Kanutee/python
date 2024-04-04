lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')

with open('life.csv', 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split(',')
        life_expectancy = float(parts[3])
        if life_expectancy < lowest_life_expectancy:
            lowest_life_expectancy = life_expectancy
        if life_expectancy > highest_life_expectancy:
            highest_life_expectancy = life_expectancy

print(f"The lowest life expectancy is: {lowest_life_expectancy}")
print(f"The highest life expectancy is: {highest_life_expectancy}")
