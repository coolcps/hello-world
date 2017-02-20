from geojson import Feature, Point, FeatureCollection, LineString
import geojson
import csv
from pprint import pprint

import csv
from itertools import chain

d = {}
with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        d[row['Office']] = row

pprint(d)

features = []
for k, v in d.items():
    p1 = Point((float(v['Longitude']),float(v['Latitude'])))
    features.append(Feature(geometry=p1, properties=v))

fc = FeatureCollection(features)
dump = geojson.dumps(fc, sort_keys=True)
pprint(fc)

with open('bldg.geojson', 'w') as outfile:
    outfile.write(dump)



features = []
for k, v in d.items():
    if v['Connectivty_1']!= '':
        contype, site, speed, cktid = v['Connectivty_1'].split(':')
        l1 = LineString([(float(v['Longitude']),float(v['Latitude'])), (float(d[site]['Longitude']),float(d[site]['Latitude']))])
        features.append(Feature(geometry=l1, properties={'type': contype, 'speed': speed, 'cktid': cktid}))
    if v['Connectivty_2'] != '':
        contype, site, speed, cktid = v['Connectivty_2'].split(':')
        l1 = LineString([(float(v['Longitude']),float(v['Latitude'])), (float(d[site]['Longitude']),float(d[site]['Latitude']))])
        features.append(Feature(geometry=l1, properties={'type': contype, 'speed': speed, 'cktid': cktid}))

fc = FeatureCollection(features)

dump = geojson.dumps(fc, sort_keys=True)
pprint(fc)
with open('ckt.geojson', 'w') as outfile:
    outfile.write(dump)