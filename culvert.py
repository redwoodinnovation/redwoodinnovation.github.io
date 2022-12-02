import overpass
import geojson

api = overpass.API(timeout=1500)

# api.get returns a FeatureCollection
res = api.get("""
  area(id:3602999142);
  (
    nwr["tunnel"="culvert"](area);
  ); 
""", verbosity='geom')

# dump as a geojson file
with open("albany/geojson/culvert.geojson",mode="w") as f:
  geojson.dump(res,f)