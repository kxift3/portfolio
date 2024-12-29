import requests

url = input("Please enter a URL: ")

try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"The website {url} is working!")
    else:
        print(f"The website {url} is not working. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Error checking the website: {e}")
