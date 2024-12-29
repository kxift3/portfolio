def calculate_stats(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    return max_temp, min_temp, mean_temp

temps = []
for _ in range(6):
    temp = float(input("Enter a temperature in Celsius: "))
    temps.append(temp)

max_temp, min_temp, mean_temp = calculate_stats(temps)
print(f"Max temperature: {max_temp}°C")
print(f"Min temperature: {min_temp}°C")
print(f"Mean temperature: {mean_temp}°C")
