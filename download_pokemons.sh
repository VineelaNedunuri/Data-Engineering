#!/bin/bash

echo "Running download_pokemons.sh"

# Read each pokemon from the file and download its data
while read -r pokemon; do
  echo "Downloading data for $pokemon"
  curl -s "https://pokeapi.co/api/v2/pokemon-species/$pokemon" -o "data/pokemons/$pokemon.json"
  sleep 2
done < "data/pokemons/pokemon_list.txt"

