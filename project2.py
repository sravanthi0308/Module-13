import requests

while True:#for more user inputs

    pokemon = input("Which pokemon do you want to find it?")
    pokemon = pokemon.lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"


    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()

        print(f"Name is\t\t{data['name']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")        
        