#!/usr/bin/env python3

import pandas as pd

poke = pd.read_csv('pokemon_data.csv')

print(poke.tail(5))

# Read header
print(poke.columns)

# Read single column 
print(poke['Name'][0:20])

# Read multiple columns
print(poke[['Name', 'Type 1', 'HP']][0:20])

# Read each rows (top 4 rows)
print(poke.head(4))

# Read a specific location
print(poke.iloc[1])
