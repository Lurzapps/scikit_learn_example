import os
import pandas as pd
import numpy as np

file_old = '../datasets/Melbourne_old.csv'
file_new = '../datasets/Melbourne.csv'
file_descriptor = '../datasets/Melbourne.txt'

# read
data = pd.read_csv(file_old, sep=';', quotechar='"', skipinitialspace=True,
                   names=['price', 'landsize', 'building_area', 'lat', 'lng', 'bedrooms'])

# combine the area column
new_areas = []

for i in range(len(data['landsize'])):
    building_area = str(data['building_area'][i])
    landsize = str(data['landsize'][i])

    if building_area != 'nan':
        app = building_area
    else:
        app = landsize

    if '.' in app:
        app_p_idx = app.find('.')
        napp = app.replace('.', '')
        a_app = napp[:app_p_idx] + '.' + napp[app_p_idx:]
        new_areas.append(a_app)
    else:
        new_areas.append(app)

# add column and bring it in the right position with excel afterwards
data['area'] = pd.DataFrame(new_areas)

# delete old size area columns
del data['landsize']
del data['building_area']

# correct the lat / lng numbers (they have to many points in them)
# after the first point remove all other points
new_lats, new_lngs = [], []

for i in range(len(data['lat'])):
    lat = str(data['lat'][i])
    lng = str(data['lng'][i])

    lat_p_idx = lat.find('.')
    nlat = lat.replace('.', '')
    a_lat = nlat[:lat_p_idx] + '.' + nlat[lat_p_idx:]
    new_lats.append(a_lat)

    lng_p_idx = lng.find('.')
    nlng = lng.replace('.', '')
    a_lng = nlng[:lng_p_idx] + '.' + nlng[lng_p_idx:]
    new_lngs.append(a_lng)


data['lat'] = pd.DataFrame(new_lats)
data['lng'] = pd.DataFrame(new_lngs)

# save again
data.to_csv(file_new, mode='w', sep=';', index=False)
