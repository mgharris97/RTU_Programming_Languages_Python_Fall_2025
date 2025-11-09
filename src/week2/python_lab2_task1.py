"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [64, 60, 56, 42, 40]
city_population = {"Riga": 632614, "New York": 8419600, "Berlin": 3769000, "London": 8982000, "Tokyo": 13929286}

# TODO: Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get) #this works. Not sure why it's showing an error
largest_population = max(city_population.values())
total_population = sum(city_population.values())

# TODO: Print results
print(f"Average temperature: {average_temperature} degrees fahrenheit")
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
