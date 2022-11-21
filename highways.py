import overpass
import geojson

api = overpass.API(timeout=500)

# api.get already returns a FeatureCollection, a GeoJSON type
res = api.get("""
  nwr(37.8885,-122.2966,37.8906,-122.2945)->.all;
  (
    way.all[highway];
    nwr.all[leisure=swimming_pool];
    nwr.all[leisure=track];
    nwr.all[leisure=pitch];
    nwr.all[leisure=sports_center];
    nwr.all[service=driveway];
    nwr.all[man_made=flagpole];
    nwr.all["garden:type"="community"];
    nwr.all["garden:type"="school"];
    nwr.all[leisure=garden];
    nwr.all[landuse=allotments];
    nwr.all[barrier=gate];  
  ); 
""", verbosity='geom')

# dump as file, if you want to save it in file
with open("albany/cornell/geojson/highways.geojson",mode="w") as f:
  geojson.dump(res,f)