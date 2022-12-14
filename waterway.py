import overpass
import geojson

api = overpass.API(timeout=1500)

# api.get returns a FeatureCollection
res = api.get("""

 nwr["waterway"](37.833333,-122.383333,37.9,-122.233611);

""", verbosity='geom')

# dump as a geojson file
with open("geojson/waterway.geojson",mode="w") as f:
  geojson.dump(res,f)