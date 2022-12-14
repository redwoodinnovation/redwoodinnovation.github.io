import overpass
import geojson

api = overpass.API(timeout=500)

# api.get returns a FeatureCollection. 
res = api.get("""

  (
    nwr["leisure"="garden"](37.833333,-122.383333,37.9,-122.233611);
    nwr["garden:type"](37.833333,-122.383333,37.9,-122.233611);
    nwr["garden"](37.833333,-122.383333,37.9,-122.233611);
    );

""", verbosity='geom')

# dump as a geojson file 
with open("geojson/garden.geojson",mode="w") as f:
  geojson.dump(res,f)