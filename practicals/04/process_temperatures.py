def calculate_stats(temperatures):
    max_temp = max(temperatures)
    min_temp = min(temperatures)
    mean_temp = sum(temperatures) / len(temperatures)
    return max_temp, min_temp, mean_temp

temps = []
while True:
    temp_input = input("Enter a temperature in Celsius (press Enter to see results): ")
    if not temp_input:
        break
    temps.append(float(temp_input))

if temps:
    max_temp, min_temp, mean_temp = calculate_stats(temps)
    print(f"Max temperature: {max_temp}°C")
    print(f"Min temperature: {min_temp}°C")
    print(f"Mean temperature: {mean_temp}°C")
else:
    print("No temperatures entered.")
