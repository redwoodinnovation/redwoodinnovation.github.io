# Cornell Elementary School 

A Github webpage displaying 1) circle (nodes) which change color or size and 2) single polygons (areas) which may change color in respone to changes in a Google Sheet values.

## Sensor Data

- The property shape displays the CO2 value per the CO2 color gradient. Data from 4pm the previous day pulled into a Google Sheet via Google Apps Script each morning between 9 and 10 AM. 

- CO2 levels shown per room are manually entered in a Google Sheet.  

- CO2 - Crowdsense values are entered into a Google Sheet by way of a Google Form, wherein participants enter longitude, latitude, Room # (when applicable), and CO2 ppm values. 

## Resource Data

- Electricity (kWh), natural gas (kBTU), and water (gal) are manually entered into a Google Sheet by way of a Google Form.

## Geometry

- Geometry is rendered using d3.js

- Building plan polygons are geojson and are tagged as Level 0 or Level 1. 

- Streets and building outlines are geojson.

- Tree and entrance nodes are loaded per bounding box via Overpass API.

## Data

- Room sensors data are stored in the "Cornell room sensors" Google Sheet.

- 4PM exterior CO2 data are stored in the "Picarro4PM" Google Sheet.

- Meter data are entered in the Google Form "Meter Reading Form" and are stored in the associated Google Sheet.

- CO2 Crowdsense data are entered in the Google Form "CO2 Crowdsense" and are stored in the associated Google Sheet. 


