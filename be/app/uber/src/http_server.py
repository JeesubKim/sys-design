
import sys
import os
import argparse
sys.path.append(os.path.join(os.path.dirname(__file__), "server"))

from concurrent.futures import ThreadPoolExecutor
import grpc
from server.location_pb2_grpc import add_LocationServiceServicer_to_server
from server.location_app import LocationService
# from server.match_app import 
# from server.match_pb2 import add_MatchServiceServicer_to_server

def start_server(port:int, add_servicer_to_server:callable, service):
    print("Server start...", service, "at: ", port)
    
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_servicer_to_server(service(), server)
    
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="server")
    parser.add_argument('--port', type=int, help='Port', required=True)
    args = parser.parse_args()
    start_server(args.port, add_LocationServiceServicer_to_server, LocationService)
    # start_server(50052, add_LocationServiceServicer_to_server, LocationService)
    # start_server(50052, add_MatchServiceServicer_to_server, )