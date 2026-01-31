import requests

def gardening(item):
    api = "sk-BqiT67f65622744359696"
    url = f"https://perenual.com/api/v2/species-list?key={api}&q={item}"
    response = requests.get(url)
    if response.status_code == 200 and response.status_code == 200:
        data = response.json()
        if "data" in data:
            plant = data["data"][0]
            print(f"Plant name: {plant.get('common_name', 'N/A')}")
            print(f"Scientific Name: {plant.get('scientific_name', 'N/A')}")
            print(f"Family: {plant.get('family', 'N/A')}")
    else:
        print("Plant not found")