from flask import Flask, jsonify, Response
import requests
import json
import collections

app = Flask(__name__)

@app.route("/", methods=["GET"])
def start():
    return Response(
        response=f"OAK: Now it IS the time to do that",
        status=200,
    )


@app.route('/pokedex/<string:pokemon_name>/<int:limit>', methods=["GET"])

def get_pokemons(pokemon_name, limit) -> list:
    api_url = f'https://pokeapi.co/api/v2/pokemon/?limit={1500}'
    response = requests.get(url=api_url)
    response_api = response.json()
    offset_start = 0
    for key in response_api["results"]:
        offset_start += 1
        if pokemon_name in key['name']:
            break
    api_url = f'https://pokeapi.co/api/v2/pokemon/?offset={offset_start-1}&limit={limit}'
    response = requests.get(url=api_url)
    response_api = response.json()
    return jsonify({'name_contains': pokemon_name, 'offset': offset_start, 'limit': limit, 'data': response_api})

@app.route('/pokedex/pokemon/<string:pokemon_name>', methods=["GET"])

def getPokemon(pokemon_name) -> list:
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}/'
    response = requests.get(url=api_url)
    response_api = response.json()
    pokemon_data = json.dumps(response_api)
    pokemon_data = json.loads(pokemon_data)
    return jsonify({
        'abilities': pokemon_data.get('abilities'), 
        'base_experience': pokemon_data.get('base_experience'),
        'forms': pokemon_data.get('forms'),
        'height': pokemon_data.get('height'),
        'id': pokemon_data.get('id'),
        'location_area_encounters': pokemon_data.get('location_area_encounters'),
        'moves': pokemon_data.get('moves'),
        'name': pokemon_data.get('name'),
        'order': pokemon_data.get('order'),
        'species': pokemon_data.get('species'),
        'sprites': pokemon_data.get('sprites'),
        'stats': pokemon_data.get('stats'),
        'types': pokemon_data.get('types'),
        'weight': pokemon_data.get('weight')
    })

if __name__ == "__main__":
	app.run(debug=True)