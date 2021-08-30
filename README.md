# poke-api
coding challenge pokemon


# Pre Requirements
* **Python 3**-**pipenv**

# Setup Python Virtual Environment #
```cmd
pip install pipenv
```
**Windows** CMD:
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install -e .
```
**Linux / MAC** command:
```cmd
python -m venv venv
source venv/bin/activate
python -m pip install -e .
```

**Running Python Script**:
```cmd
python app.py
```
# Endpoints

## Global search
It works going to the following address 
```
/pokedex/pokemon_name/limit
```

  Where pokemon_name can be a partial name and limit is just the number of pokemons that will appear after the first pokemon found by the pokedex

  The pokemon_name is string
  The limit is an integer

  If there is no pokemon containing that string, then the search will return an ampty search

## Search by name
It works on the address 
```
/pokedex/pokemon/pokemon_name
```
  In this case, the pokemon_name has to be correct, or the search will return empty
