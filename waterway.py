import overpass
import geojson

api = overpass.API(timeout=1500)

# api.get returns a FeatureCollection
res = api.get("""
 nwr["waterway"](37.881364,-122.329245,37.904963,-122.258104);
""", verbosity='geom')

# dump as a geojson file
with open("albany/geojson/waterway.geojson",mode="w") as f:
  geojson.dump(res,f)