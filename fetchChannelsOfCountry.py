import requests

API_TOKEN = "INSERT-YOUR-API-TOKEN-HERE"
BASE_URL = "https://tv-plan.org/api-v1.php"

# REPLACE this ID based on the Country where you want to fetch the channels from
countryID = "133"

params = {
    "apitoken": API_TOKEN,
    "resource": "channelsOfCountry",
    "countryId" : countryID
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if "error" in data:
    print(data)
    pass
else:
    print("Channels for Country ID < "+str(countryID)+" >:")
    for channel in data:
        print("- UID: "+channel["uid"]+" / Display Name: "+channel["display_name"])
    pass

