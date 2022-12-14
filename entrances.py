import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection
res = api.get("""

    node["entrance"](37.833333,-122.383333,37.9,-122.233611);

""", verbosity='geom')

# dump as a geojson file
with open("geojson/entrances.geojson",mode="w") as f:
  geojson.dump(res,f)