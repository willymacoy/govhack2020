# postcode
Python function to return polygon enclosing GPS coordinates

### Open data

https://discover.data.vic.gov.au/dataset/vicmap-admin

We use gps coordinates from the phone app and the postcode polygons to establish where the user is located. The postcode data is stored in the project database to make it quicker to work with - rather than figuring it out every time we analyse the data

### Files

postcode - python cgi script

melbournesamples.ipynb - generate sample data

bottle.py - python bottle server version

### To do

- to be made a AWS lambda function
- the postcode file is 20MB
  - reading this off disk every time might be excessive
  - can we keep it in memory?
  - there are 700 postcode polygons, each with thousands of vertices
    - could create a file with enclosing boxes as the polygons
      - read only postcodes that GPS coords are in enclosing box?
    - what about an array of centrepoints
      - calc distance to each centre point
      - and check each polygon in order
    - both solutions would require a file for each postcode

### Demo

As at 16 August 2020

http://54.206.23.77/govhack/postcode?latitude=-37.69&longitude=145.05