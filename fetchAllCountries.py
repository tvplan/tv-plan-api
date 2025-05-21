import requests

API_TOKEN = "INSERT-YOUR-API-TOKEN-HERE"
BASE_URL = "https://tv-plan.org/api-v1.php"

params = {
    "apitoken": API_TOKEN,
    "resource": "countries"
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if "error" in data:
    print(data)
    pass
else:
    print("Available Countries:")
    for country in data:
        print("- Clear Name: "+country["name"]+" / Display Name: "+country["display_name"])
    pass

