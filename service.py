import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection
res = api.get("""
    area(id:3600396499);  (
    way["service"](area);
  ); 
""", verbosity='geom')

# dump as a geojson file
with open("geojson/service.geojson",mode="w") as f:
  geojson.dump(res,f)