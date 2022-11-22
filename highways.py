import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection, a GeoJSON type
res = api.get("""
  nwr(37.8885,-122.2966,37.8906,-122.2945)->.all;
  (
    way.all[highway];
  ); 
""", verbosity='geom')

# dump as file, if you want to save it in file
with open("albany/cornell/geojson/highways.geojson",mode="w") as f:
  geojson.dump(res,f)