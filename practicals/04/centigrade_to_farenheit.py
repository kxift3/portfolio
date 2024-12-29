def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperature = input("Enter a temperature in Centigrade (e.g. 25C): ")
celsius_value = float(temperature[:-1])
fahrenheit_value = convert_celsius_to_fahrenheit(celsius_value)
print(f"{celsius_value}C = {fahrenheit_value}F")
