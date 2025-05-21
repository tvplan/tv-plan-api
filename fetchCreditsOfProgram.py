import requests

API_TOKEN = "INSERT-YOUR-API-TOKEN-HERE"
BASE_URL = "https://tv-plan.org/api-v1.php"

# REPLACE this ID based on the Program where you want to fetch the data from
programID = "61173144"

params = {
    "apitoken": API_TOKEN,
    "resource": "creditsOfProgram",
    "programId" : programID
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if "error" in data:
    print(data)
    pass
else:
    print("Credits of Program ID < "+str(programID)+" >:")
    for credit in data:    
        print("- Job: "+credit["job"]+" / Name: "+credit["name"])
    pass
