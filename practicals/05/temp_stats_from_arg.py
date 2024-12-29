import sys

if len(sys.argv) > 1:
    temps = [float(temp) for temp in sys.argv[1:]]
    max_temp = max(temps)
    min_temp = min(temps)
    mean_temp = sum(temps) / len(temps)

    print(f"Max temperature: {max_temp}°C")
    print(f"Min temperature: {min_temp}°C")
    print(f"Mean temperature: {mean_temp}°C")
else:
    print("No temperatures provided.")
