import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection
res = api.get("""
    nwr["amenity"="school"](37.8436814502461,-122.3103618621826,37.89314382849696,-122.2309684753418);
""", verbosity='geom')

# dump as a geojson file
with open("berkeley/geojson/schoolgrounds.geojson",mode="w") as f:
  geojson.dump(res,f)