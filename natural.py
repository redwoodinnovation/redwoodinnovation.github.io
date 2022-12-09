import overpass
import geojson

api = overpass.API(timeout=1000)

# api.get returns a FeatureCollection
res = api.get("""
    area(id:3600396499);
    nwr["natural"]["natural"!~"tree"]["natural"!~"bay"]["natural"!~"coastline"]["natural"!~"water"]["natural"!~"wetland"](area);
""", verbosity='geom')

# dump as a geojson file
with open("geojson/natural.geojson",mode="w") as f:
  geojson.dump(res,f)