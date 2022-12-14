import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection. Here, leisure=garden is excluded (is included at garden.py)
res = api.get("""

    way["leisure"]["leisure"!~"garden"](37.833333,-122.383333,37.9,-122.233611);

""", verbosity='geom')

# dump as a geojson file 
with open("geojson/leisure.geojson",mode="w") as f:
  geojson.dump(res,f)