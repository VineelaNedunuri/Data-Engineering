#!/bin/bash
echo "running initializations"


for pokemon in $(cat data/pokemons/pokemon_list.txt); do
  echo "Requesting API for $pokemon"
  curl -s "https://pokeapi.co/api/v2/pokemon-species/$pokemon" -o "data/pokemons/$pokemon.json"
  sleep 2
done < data/pokemons/pokemon_list.txt
