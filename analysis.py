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
print('-------top 4----------')
print(poke.head(4))

# Read a specific location
print('-------iloc 1----------')
print(poke.iloc[1])

# Read multiple rows
print('-------iloc 1-4 -------')
print(poke.iloc[1:4])

# Read specific location
print(poke.iloc[2,1])

# Loop through and read each row
print('-------loop read each row -------')
for index, row in poke.iterrows():
    print(index, row[['Name', 'HP']])

##
print('-------look for rows with condition -------')
print(poke.loc[poke['Type 1'] == "Fire"])
