import math
from model.parking import *
from api import db

def _getSquareFixedPositions(longitude, latitude, distance):
    EARTH_RADIUS = 6371

    #角度转弧度
    def deg2rad(deg):
        return math.radians(deg)

    d_lng = 2 * math.asin(math.sin(distance / (2 * EARTH_RADIUS)) / math.cos(deg2rad(latitude)))
    d_lng = deg2rad(d_lng)
    d_lat = distance / EARTH_RADIUS
    d_lat = deg2rad(d_lat)

    left_top = {'lat': latitude + d_lat, 'lng': longitude - d_lng}
    right_top = {'lat': latitude + d_lat, 'lng': longitude + d_lng}
    left_bottom = {'lat': latitude - d_lat, 'lng': longitude - d_lng}
    right_bottom = {'lat': latitude - d_lat, 'lng': longitude + d_lng}

    return left_top, right_top, left_bottom, right_bottom

def searchNearByParkings(longitude, latitude, distance=0.5):
    square = _getSquareFixedPositions(longitude, latitude, distance)
    print(square)
    left_top = square[0]
    right_top = square[1]
    left_bottom = square[2]
    right_bottom = square[3]

    #$info_sql = "select id,locateinfo,lat,lng from `lbs_info` where lat<>0 and lat>{$squares['right-bottom']['lat']} " \
    #            "and lat<{$squares['left-top']['lat']} and lng>{$squares['left-top']['lng']} and lng<{$squares['right-bottom']['lng']} ";

    #查询周边满足条件的100个停车场
    result = db.session.query(PARKING).filter(PARKING.location_y != 1, PARKING.location_y > right_bottom['lat'], PARKING.location_y < left_top['lat'], PARKING.location_x > left_top['lng'], PARKING.location_x < right_bottom['lng']).limit(100)
    #print(result.all())
    return result
