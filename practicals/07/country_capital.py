country_capitals = {}

while True:
    country = input("Enter a country name (or type 'q' to end the conversation): ").strip().title()
    if country.lower() == 'q':
        break
    if country in country_capitals:
        print(f"The capital of {country} is {country_capitals[country]}.")
    else:
        capital = input(f"What is the capital of {country}? ").strip().title()
        country_capitals[country] = capital
        print(f"{capital} has been added as the capital of {country}.")
