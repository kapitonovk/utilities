import csv
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os, shutil

def json_cleaner(filename, json_folder):

    with open(f'{json_folder}/{filename}.json', 'r') as f:
        data = f.read()

    data = data.split('"items":[{')[1]
    data = data.split('},{')

    dumper = {'id':[], 'name':[], 'lat':[], 'lon':[], 'address_name':[]}

    for x in data:
        for i in x.split(',"'):
            i = i.replace('":"', ':')
            i = i.replace('"', '')
            i = i.replace('{', '')
            i = i.replace('}', '')
            i = i.replace('point:', '')
            # print(i)
            for j in dumper.keys():
                if j == i.split(':')[0]:
                    key_ = i.split(':')[0]
                    val_ = i.split(':')[1]
                    swap = dumper[key_]
                    swap.append(val_)
                    dumper[key_] = swap
        
        # swap = dumper['geometry']
        # swap.append(f'POINT {float(dumper["lat"][-1]), float(dumper["lon"][-1])}')
        # dumper['geometry'] = swap
 
    # print(dumper)
    # print(10*'\n')
    dump = pd.DataFrame(dumper)
    dump.to_csv(f'csv/{filename}.csv')

def csv_to_gis(filename, lon, lat, format):
    dump = pd.read_csv(f'csv/zz_fin/{filename}.csv')

    gdf = gpd.GeoDataFrame(
    dump, geometry=gpd.points_from_xy(dump[lon], dump[lat]), crs='EPSG:4326')

    gdf = gdf.to_crs(32637)

    gdf.to_file(f'gis/{filename}.{format.lower()}', driver=format)


print(50 * '=' + 40 * '\n')

os.chdir(__file__[:__file__.rfind('/'):])

if 'csv' not in os.listdir():
    os.mkdir('csv')

if 'gis' not in os.listdir():
    os.mkdir('gis')

json_folder = input('json folder name: ')
json = os.listdir(json_folder)

if input('format: (G)PKG or Geo(J)son?').lower() == 'g':
    format = 'GPKG'
else:
    format = 'GeoJSON'

for i in sorted(json):
    filename = i.split('.')[0]
    if '.json' in i:
        lon = 'lon'
        lat = 'lat'
        print(filename)
        json_cleaner(filename, json_folder)
        # csv_to_gis(filename, lon, lat, format)

csv_dir = os.listdir('csv')

### csv unifier

if 'zz_fin' not in csv_dir:
    os.mkdir('csv/zz_fin')
else:
    shutil.rmtree('csv/zz_fin')
    os.mkdir('csv/zz_fin')



for i in csv_dir:
    zz_fin = os.listdir('csv/zz_fin')
    x = ''.join([a for a in i if not a.isdigit()])
    if x not in zz_fin and '.csv' in i:
        # d = open(f'csv/{i}').read()
        data = pd.read_csv(f'csv/{i}')
        for j in csv_dir:
            if i != j and 'csv' in j:
                y =  ''.join([a for a in j if not a.isdigit()])
                if x == y:
                    df = pd.read_csv(f'csv/{j}')
                    data = pd.concat([data, df], ignore_index=True)

        drop = data[['id', 'name', 'lat', 'lon', 'address_name']]
        drop.to_csv(f'csv/zz_fin/{x}')



## transform csv to gpkg
zz_fin = os.listdir('csv/zz_fin')

for i in zz_fin:
        if ".csv" in i:
            filename = i.split('.')[0]
            lon = 'lon'
            lat = 'lat'
            print(filename)
            csv_to_gis(filename, lon, lat, format)