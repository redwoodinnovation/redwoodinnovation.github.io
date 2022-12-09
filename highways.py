import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection. Here, highway=service is excluded (is included at service.py)
res = api.get("""
  area(id:3600396499);
  way["highway"]["highway"!~"service"]["highway"!~"cycleway"](area); 
""", verbosity='geom')

# dump as a geojson file
with open("geojson/highways.geojson",mode="w") as f:
  geojson.dump(res,f)