import os
import pandas as pd

file_old = '../datasets/Delhi_old.csv'
file_new = '../datasets/Delhi.csv'
file_descriptor = '../datasets/Delhi.txt'


def column_names() -> list:
    with open(file_descriptor, 'r') as f:
        return f.read().splitlines()[0].split(';')


# read
data = pd.read_csv(file_old, sep=';', quotechar='"', skipinitialspace=True, names=column_names())

# index the locations with unique ids (in a map / dictionary)
locations = dict()
lastId = 0

for loc in data['loc']:
    if loc not in locations:
        lastId += 1
        locations[loc] = lastId

# write these locations in the column
new_loc = []
for loc in data['loc']:
    new_loc.append(locations[loc])

data['loc'] = pd.DataFrame(new_loc)

# save again
data.to_csv(file_new, sep=';', mode='w', index=False)
