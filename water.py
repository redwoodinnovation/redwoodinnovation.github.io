import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection
res = api.get("""
  area(id:3600396499);
  (
    nwr["natural"="wetland"](area);
    nwr["natural"="water"](area);
    nwr["water"](area);
  ); 
""", verbosity='geom')

# dump as a geojson file
with open("geojson/water.geojson",mode="w") as f:
  geojson.dump(res,f)