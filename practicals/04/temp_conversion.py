def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C = {fahrenheit}°F")

fahrenheit_input = float(input("Enter temperature in Fahrenheit: "))
celsius_output = fahrenheit_to_celsius(fahrenheit_input)
print(f"{fahrenheit_input}°F = {celsius_output}°C")
