from api import app
from api import db
from service import mapService
from model import *
from flask import Flask, render_template, session, request, redirect, url_for
from flask import jsonify, abort


#[api list]
@app.route('/endpoints',methods=['GET'])
def api_list():
    return jsonify({'list': 'yes'})


'''
地图上搜索附近的停车场 
    @param: location_x 经度
    @param: location_y纬度
    @param: distance 方圆(千米)
    @param: conditions 查询条件 (可选)
    
    @return: 满足条件的停车场json数据，包括：停车场名称、经纬度、状态、运营情况
'''
@app.route('/api/nearbyParkings',methods=['GET','POST'])
def nearbyParkings():
    try:
        location_x = request.json["location_x"]
        location_y = request.json["location_y"]
        distance = request.json["distance"]

        result = mapService.searchNearByParkings(float(location_x), float(location_y), float(distance))

        parkings = []

        for parking in result:
            rs = {}
            rs['name'] = parking.name
            rs['location_y'] = parking.location_y
            rs['location_x'] = parking.location_x
            rs['address'] = parking.address
            rs['photos'] = parking.photos
            rs['service_spaces'] = parking.service_spaces
            rs['service_kind'] = parking.service_kind
            rs['service_time'] = parking.service_time
            rs['type'] = parking.type
            rs['state'] = parking.state
            rs['uuid'] = parking.uuid
            parkings.append(rs)
        #print(parkings)
    except Exception as ex:
        print(repr(ex))

    return jsonify({'parkings': parkings})