import overpass
import geojson

api = overpass.API(timeout=1500)

# api.get already returns a FeatureCollection
res = api.get("""
    area(id:3600396499);
    nwr["amenity"="school"](area);
 """, verbosity='geom')

# dump as a geojson file
with open("geojson/schoolgrounds.geojson",mode="w") as f:
  geojson.dump(res,f)