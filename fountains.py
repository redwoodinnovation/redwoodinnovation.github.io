import overpass
import geojson

api = overpass.API(timeout=1500)

# api.get returns a FeatureCollection
res = api.get("""
  area(id:3600396499);
  (
    node["amenity"="fountain"](area);
  ); 
""", verbosity='geom')

# dump as a geojson file
with open("geojson/fountain.geojson",mode="w") as f:
  geojson.dump(res,f)