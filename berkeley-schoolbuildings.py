import overpass
import geojson

api = overpass.API(timeout=1000)

# api.get already returns a FeatureCollection
res = api.get("""
(
  way[building](poly:"37.86871 -122.272573 37.868942 -122.27077 37.868942 -122.270688 37.868921 -122.270637 37.868887 -122.270591 37.868863 -122.270571 37.86884 -122.270562 37.867306 -122.270404 37.867151 -122.270376 37.866354 -122.27028 37.865552 -122.270194 37.865537 -122.2702 37.865522 -122.270223 37.865276 -122.272114 37.865295 -122.272169 37.865331 -122.272203 37.866952 -122.272384");  
);
""", verbosity='geom')

# dump as a geojson file
with open("berkeley/geojson/schoolbuildings.geojson",mode="w") as f:
  geojson.dump(res,f)