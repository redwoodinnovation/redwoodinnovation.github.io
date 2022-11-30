import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection. Here, leisure=garden is excluded (is included at garden.py)
res = api.get("""
  area(id:3602999142);
  (
    way["leisure"]["leisure"!~"garden"](area);
  ); 
""", verbosity='geom')

# dump as a geojson file 
with open("albany/geojson/leisure.geojson",mode="w") as f:
  geojson.dump(res,f)