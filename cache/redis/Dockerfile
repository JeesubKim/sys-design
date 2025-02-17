# Redis 공식 이미지 사용
FROM redis:latest

# Redis 설정 파일 추가 (선택 사항)
COPY redis.conf /usr/local/etc/redis/redis.conf


# Redis 실행 (설정 파일 적용)
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
