import requests

API_TOKEN = "INSERT-YOUR-API-TOKEN-HERE"
BASE_URL = "https://tv-plan.org/api-v1.php"

# REPLACE this ID based on the Channel where you want to fetch the programs from
channelID = "23558"

params = {
    "apitoken": API_TOKEN,
    "resource": "programsOfChannel",
    "channelId" : channelID
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if "error" in data:
    print(data)
    pass
else:
    print("Programs of Channel ID < "+str(channelID)+" >:")
    for program in data:    
        print("- Title: "+program["title"]+" / Start Time: "+program["start"] +" -> End Time: "+program["stop"])
    pass

