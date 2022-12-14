import overpass
import geojson

api = overpass.API(timeout=1000)

# api.get returns a FeatureCollection
res = api.get("""

  (
    node["natural"]["natural"!~"tree"]["natural"!~"bay"]["natural"!~"coastline"]["natural"!~"water"]["natural"!~"wetland"](37.833333,-122.383333,37.9,-122.233611);
    way["natural"]["natural"!~"tree"]["natural"!~"bay"]["natural"!~"coastline"]["natural"!~"water"]["natural"!~"wetland"](37.833333,-122.383333,37.9,-122.233611);
  );

""", verbosity='geom')

# dump as a geojson file
with open("geojson/natural.geojson",mode="w") as f:
  geojson.dump(res,f)