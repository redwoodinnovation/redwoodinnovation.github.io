import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection
res = api.get("""
   (way[building](poly:"37.8889747 -122.2949514 37.8888376 -122.2956308 37.8894885 -122.295121 37.8903283 -122.2961314 37.8903653 -122.2954079 37.8901303 -122.2953348 37.8900959 -122.2960687 37.8899635 -122.2960219");  
); 
""", verbosity='geom')

# dump as a geojson file
with open("albany/geojson/schoolbuildings.geojson",mode="w") as f:
  geojson.dump(res,f)