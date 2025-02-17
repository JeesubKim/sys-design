poetry run python -m grpc_tools.protoc -I=proto --python_out=./server --grpc_python_out=./server proto/*.proto

protoc -I=proto --go_out=. --grpc-gateway_out=. --openapiv2_out=. --go-grpc_out=. proto/*.proto