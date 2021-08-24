import requests, csv

faceit_url = "https://open.faceit.com/data/v4/rankings/games/csgo/regions/{region}?offset={offset}&limit={limit}"
headers = {"Authorization": "Bearer c32a2756-b62f-44e3-9b5c-28fdedebc731"}

eu_players = 8849400
na_players = 937100

def get_elo_data(region, players):
    elo=[]
    for chunk in range(0, players, 100):
        data = requests.get(url = faceit_url.format(region = region, offset = chunk, limit = 100), headers = headers).json()
        for item in data["items"]:
            elo.append(item["faceit_elo"])
        print("Fetched {} chunk {} - {}".format(region, chunk, chunk+100))

    return elo
    
region_dict = {"EU":8849400, "US":937100}
for region in region_dict:
    elo_data = get_elo_data(region, region_dict[region])
    file = open(region, "w")
    writer = csv.writer(file)
    writer.writerow(elo_data)
    file.close()
