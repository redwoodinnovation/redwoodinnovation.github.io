import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection
res = api.get("""
  area(id:3602999142);
  (
    nwr["barrier"](area);
  ); 
""", verbosity='geom')

# dump as a geojson file
with open("albany/geojson/barrier.geojson",mode="w") as f:
  geojson.dump(res,f)