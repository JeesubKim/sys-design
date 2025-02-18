from concurrent.futures import ThreadPoolExecutor
import grpc
from location_pb2 import Location, GetDriverLocationRequest, GetUserLocationRequest, UpdateLocationRequest
from match_pb2 import Estimation, EstimateRequest, EstimateResponse, Match, MatchRequest, UpdateMatchRequest, ListMatchesRequest, ListMatchesResponse
import match_pb2_grpc
from datetime import datetime
from google.protobuf.json_format import MessageToDict, ParseDict
import redis
from pymongo import MongoClient 
from datetime import datetime

location_db = redis.StrictRedis(host='localhost', port=6379, db=0)
# from bson import ObjectId
mongo_client = MongoClient("mongodb://root:root@localhost:27017/")
# print("mongo_client", mongo_client)
db = mongo_client["uber"]
m_collections = db["match"]
e_collections = db["estimation"]
print(location_db)
print(e_collections)


class MatchService(match_pb2_grpc.MatchService):

    def estimate(self, request:EstimateRequest, context) -> EstimateResponse :
        print(request)
        data = {
            "user_id":request.parent,
            "starting_location": {
                "lng": request.starting_location.lng,
                "lat": request.starting_location.lat
            },
            "destination": {
                "lng": request.destination.lng,
                "lat": request.destination.lat
            },
            "eta":"15min",
            "fare":"$120",
            "status":"Pending",
            "range": "NA",
            "created_at": str(datetime.now())
        }
        
        result = e_collections.insert_one(data)
        estimation_id = str(result.inserted_id)
        data["estimation_id"] = estimation_id
        del data["_id"]
        print("data:", data)

        # print(result, estimation_id)
        response = EstimateResponse()
        ParseDict({
                "estimation":data
                # "estimation": {
                #     **data,
                #     "estimation_id":estimation_id
                # }
            }, response)
        
        print(response)
        return response
    def match(self, request:MatchRequest, context)-> Match:

        print("Match Request", request)
    
    def updateMatch(self, request:UpdateMatchRequest, context) -> Match:...
    def ListMatches(self, request:ListMatchesRequest, context) -> ListMatchesResponse:...

    
