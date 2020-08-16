# postcode
Python function to return polygon enclosing GPS coordinates

### Open data

https://discover.data.vic.gov.au/dataset/vicmap-admin

We use gps coordinates from the phone app and the postcode polygons to establish where the user is located. The postcode data is stored in the project database to make it quicker to work with - rather than figuring it out every time we analyse the data

### Files

postcode - python cgi script

melbournesamples.ipynb - generate sample data

### To do

- to be made a AWS lambda function

### Demo

As at 16 August 2020

http://54.206.23.77/govhack/postcode?latitude=-37.69&longitude=145.05