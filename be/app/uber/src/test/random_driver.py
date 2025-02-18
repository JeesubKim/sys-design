import threading
import time
import random
import requests
import math
import signal
import sys

# 초기 설정
START_LAT = 47.598693
START_LNG = -122.035366
BASE_URL = "http://localhost:8080/api/v1/location"
EARTH_RADIUS = 3958.8  # 지구 반지름 (마일)
MOVEMENT_SPEED = 10 / 3600  # 10mph -> degrees/sec

# 랜덤 위치 생성 함수 (초기 위치 균등 분포)
def random_location(base_lat, base_lng, min_distance, max_distance):
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(min_distance, max_distance)

    delta_lat = (distance / EARTH_RADIUS) * (180 / math.pi)
    delta_lng = (distance / EARTH_RADIUS) * (180 / math.pi) / math.cos(math.radians(base_lat))

    new_lat = base_lat + delta_lat * math.sin(angle)
    new_lng = base_lng + delta_lng * math.cos(angle)

    return new_lat, new_lng

# 쓰레드에서 실행될 함수 (랜덤한 방향으로 계속 이동)
def thread_function(thread_id, lat, lng):
    direction = random.uniform(0, 2 * math.pi)  # 처음 이동할 랜덤 방향

    while True:
        # 일정 거리 이동 후 랜덤하게 방향을 조금씩 변경
        direction += random.uniform(-math.pi / 4, math.pi / 4)  # ±45도 랜덤 회전
        delta_lat = MOVEMENT_SPEED * math.sin(direction)
        delta_lng = MOVEMENT_SPEED * math.cos(direction) / math.cos(math.radians(lat))

        lat += delta_lat
        lng += delta_lng

        payload = {
            "parent": thread_id,
            "type": "Driver",
            "location": {"lat": str(lat), "lng": str(lng)}
        }
        print(f"Thread {thread_id}: {payload}")

        try:
            response = requests.post(BASE_URL, json=payload)
            if response.status_code == 200:
                print(f"Thread {thread_id}: Sent successfully!")
            else:
                print(f"Thread {thread_id}: Failed. {response.text}")
        except Exception as e:
            print(f"Thread {thread_id}: Error - {e}")

        time.sleep(5)  # 5초마다 이동

# 쓰레드 시작 함수 (50대씩 2개의 그룹)
def start_threads():
    threads = []
    for i in range(50):  # 0~5마일 범위
        lat, lng = random_location(START_LAT, START_LNG, 0, 5)
        thread = threading.Thread(target=thread_function, args=(i + 1, lat, lng))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    for i in range(50, 100):  # 5~10마일 범위
        lat, lng = random_location(START_LAT, START_LNG, 5, 10)
        thread = threading.Thread(target=thread_function, args=(i + 1, lat, lng))
        thread.daemon = True
        threads.append(thread)
        thread.start()

    return threads

# 메인 함수
def main():
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))
    start_threads()
    print("Threads started.")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
