import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection
res = api.get("""
  nwr(37.8885,-122.2966,37.8906,-122.2945)->.all;
  (
    nwr.all["landuse"];
  ); 
""", verbosity='geom')

# dump as a geojson file
with open("../albany/cornell/geojson/landuse.geojson",mode="w") as f:
  geojson.dump(res,f)