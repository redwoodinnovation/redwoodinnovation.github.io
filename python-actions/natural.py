import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection
res = api.get("""
    (nwr["natural"](37.8883006925662,-122.29650825262071,37.890997478019,-122.2946360707283);
    );
""", verbosity='geom')

# dump as a geojson file
with open("../albany/cornell/geojson/natural.geojson",mode="w") as f:
  geojson.dump(res,f)