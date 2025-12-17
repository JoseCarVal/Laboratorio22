import requests

url = "https://httpbin.org/get"
response = requests.get(url)

data = response.json()

print("IP:", data["origin"])
print("\nHeaders:")
for k, v in data["headers"].items():
    print(f"{k}: {v}")

print("\nArgs:", data["args"])