from concurrent.futures import ThreadPoolExecutor
import grpc
import json
from location_pb2 import Location, GetDriverLocationRequest, GetUserLocationRequest, UpdateLocationRequest
from google.protobuf.json_format import MessageToDict, ParseDict

import location_pb2_grpc
from datetime import datetime

import redis
location_db = redis.StrictRedis(host='localhost', port=6379, db=0)

print(location_db)

class LocationService(location_pb2_grpc.LocationService):
    def getUserLocation(self, request:GetUserLocationRequest, context) -> Location:

        user_location = location_db.hget("User", request.user_id)
        if user_location:
            user_location_json = json.loads(user_location)
            print("user_location:", user_location_json)
            return Location(
                **user_location_json
            )
        
        return Location(
            lat="-1",
            lng="-1"
        )
    
    def getDriverLocation(self, request:GetDriverLocationRequest, context) -> Location:
        driver_location = location_db.hget("Driver", request.driver_id)
        if driver_location:
            driver_location_json = json.loads(driver_location)
            print("driver_location:", driver_location_json)
            return Location(
                **driver_location_json
            )
        
        return Location(
            lat="-1",
            lng="-1"
        )
    
    def updateLocation(self, request:UpdateLocationRequest, context) -> None:
        print(request)
        
        id = request.parent
        user_type = request.type
        location = MessageToDict(request.location)

        location_json = json.dumps(location)
        
        try:
            print("-->", location_json)
            location_db.hset(user_type, id, location_json)

            stored_location = location_db.hget(user_type, id)
            print(user_type, id, "----> Stored Location:", stored_location)
        except Exception as e:
            print(e)

        location_db.zrem(f"{user_type}-GEO", id)
        location_db.geoadd(f"{user_type}-GEO", (float(request.location.lng), float(request.location.lat), id))
        updated_data_dict = json.loads(location_db.hget(user_type, id))
        
        return Location(
            **updated_data_dict
        )
    
