package main

import (
	"context"
	"fmt"
	"log"
	"net/http"

	"github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
	"google.golang.org/grpc"

	"grpc-gw/api/location"
	"grpc-gw/api/match"
)

func startGrpcGateway(ctx context.Context, gwMux *runtime.ServeMux) error {
	// 각 서비스별 gRPC 서버 주소 설정
	serviceEndpoints := map[string]string{
		"LocationService": "localhost:50051",
		"MatchService":    "localhost:50052",
	}

	// LocationService 핸들러 등록
	err := location.RegisterLocationServiceHandlerFromEndpoint(ctx, gwMux, serviceEndpoints["LocationService"], []grpc.DialOption{grpc.WithInsecure()})
	if err != nil {
		return fmt.Errorf("failed to register LocationService handler: %v", err)
	}

	// MatchService 핸들러 등록
	err = match.RegisterMatchServiceHandlerFromEndpoint(ctx, gwMux, serviceEndpoints["MatchService"], []grpc.DialOption{grpc.WithInsecure()})
	if err != nil {
		return fmt.Errorf("failed to register MatchService handler: %v", err)
	}

	return nil
}

func main() {
	// gRPC Gateway 설정
	ctx := context.Background()
	gwMux := runtime.NewServeMux()

	// gRPC Gateway 시작
	if err := startGrpcGateway(ctx, gwMux); err != nil {
		log.Fatalf("Failed to start gRPC Gateway: %v", err)
	}

	// HTTP 서버 실행
	log.Println("Starting HTTP server on :8080...")
	log.Fatal(http.ListenAndServe(":8080", gwMux))
}
