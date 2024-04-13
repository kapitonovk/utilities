In this repository the utility scripts for some possible purposes of an urban planner are placed

### json to gis.py 

  1. is useful if you download 2GIS API responses and have only researcher's non-commercial rights

  1. the responses are supposed to be kept in one directory, this directory and script should be kept in together

  1. the .json files with responses for one category cn be enumerated by user, later they will be merged by a program 
  (e.g. shop1.json, shop2.json, shop3.json will be merged and converted to shop.csv)

  1. the program
     - merges files with same name and various numbers
     - gets the necessary information from the 2GIS .json response
     - converts it to csv files
     - converts these csv files to either gpkg or geojson files
