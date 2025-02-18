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

	"github.com/rs/cors"
	"google.golang.org/grpc/metadata"
)

func logRequestMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		// 요청 정보 로깅
		log.Printf("Received request: %s %s", r.Method, r.URL.Path)
		log.Printf("Headers: %v", r.Header)

		// 요청 본문 로깅 (옵션, 요청 본문 크기가 클 수 있으므로 주의)
		// body, _ := ioutil.ReadAll(r.Body)
		// log.Printf("Request body: %s", string(body))

		// 요청 처리
		next.ServeHTTP(w, r)
	})
}

func startGrpcGateway(ctx context.Context, gwMux *runtime.ServeMux) error {
	// 각 서비스별 gRPC 서버 주소 설정
	serviceEndpoints := map[string]string{
		"LocationService": "localhost:50050",
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
	gwMux := runtime.NewServeMux(runtime.WithMetadata(func(ctx context.Context, req *http.Request) metadata.MD {
		return metadata.New(map[string]string{
			"user-agent": req.UserAgent(),
		})
	}))
	// gRPC Gateway 시작
	if err := startGrpcGateway(ctx, gwMux); err != nil {
		log.Fatalf("Failed to start gRPC Gateway: %v", err)
	}

	// CORS 미들웨어
	corsMiddleware := cors.New(cors.Options{
		AllowedOrigins:   []string{"*"}, // 모든 도메인 허용 (보안 필요시 제한)
		AllowedMethods:   []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
		AllowedHeaders:   []string{"Content-Type", "Authorization"},
		AllowCredentials: true,
	})
	// HTTP 서버에 미들웨어 추가하여 요청 로그를 출력
	handler := corsMiddleware.Handler(logRequestMiddleware(gwMux))
	// http.Handle("/", logRequestMiddleware(gwMux))

	// HTTP 서버 실행
	log.Println("Starting HTTP server on :8080...")
	log.Fatal(http.ListenAndServe(":8080", handler))
}
