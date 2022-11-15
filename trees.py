import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection, a GeoJSON type
res = api.get("""
    (node["natural"="tree"](37.8883006925662,-122.29650825262071,37.890997478019,-122.2946360707283);
    );
""", verbosity='geom')

# dump as file, if you want to save it in file
with open("albany/cornell/geojson/trees.geojson",mode="w") as f:
  geojson.dump(res,f)