REM poetry run python -m grpc_tools.protoc -I=proto --python_out=./server --grpc_python_out=./server proto/*.proto
REM protoc -I=proto --go_out=./grpc-gw --go-grpc_out=./grpc-gw proto/*.proto


REM Get the absolute path of the proto directory
set PROTO_DIR=%CD%\proto

REM Generate Python gRPC files
for /R proto %%f in (*.proto) do (
    poetry run python -m grpc_tools.protoc -I"%PROTO_DIR%" --python_out=./server --grpc_python_out=./server "%%f"
)

REM Generate Go gRPC files
for /R proto %%f in (*.proto) do (
    protoc -I="%PROTO_DIR%" --go_out=. --grpc-gateway_out=. --openapiv2_out=. --go-grpc_out=. "%%f"
)