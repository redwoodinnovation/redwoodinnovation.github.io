import overpass
import geojson

api = overpass.API(timeout=1500)

# api.get returns a FeatureCollection
res = api.get("""
  
    node["amenity"="fountain"](37.833333,-122.383333,37.9,-122.233611);

""", verbosity='geom')

# dump as a geojson file
with open("geojson/fountain.geojson",mode="w") as f:
  geojson.dump(res,f)