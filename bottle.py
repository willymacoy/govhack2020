#!/opt/python3.8.5/bin/python3.8
#

from bottle import route, run, request, get
import shapefile
from shapely.geometry import Polygon, Point


@route('/message')
def hello():
    return "Today is a beautiful day"

@get('/postcode')
def message():
    sf = shapefile.Reader('/opt/simple/postcode_polygon')
    shapes = sf.shapes()
    pccount = len(shapes)
    found = 0
    for pc in range(pccount) :
        rec = sf.record(pc)
        s1 = sf.shape(pc)
        geo = s1.points
        poly = Polygon(geo)
        postcode = request.query.postcode
        latitude = float(request.query.latitude)
        longitude = float(request.query.longitude)
        if poly.contains(Point(longitude,latitude)):
            found = 1
            break
        
    if (found == 1) :
        return "{0}".format(rec.POSTCODE)
    else:
        return "not found"

run(host='0.0.0.0', port=8080, debug=True)
