import threading
import time
import random
import requests
import math
import signal
import sys

# 초기 위치 (47.598693, -122.035366) 기준
START_LAT = 47.598693
START_LNG = -122.035366
BASE_URL = "http://localhost:8080/api/v1/location"
THREAD_COUNT = 10
MOVEMENT_SPEED = 10 / 3600  # 10 miles per hour in degrees per second

# 랜덤 위치 생성 함수
def random_location(base_lat, base_lng, min_distance, max_distance):
    def deg2rad(deg):
        return deg * (math.pi / 180)

    def rad2deg(rad):
        return rad * (180 / math.pi)

    earth_radius = 3958.8  # miles

    # Random angle
    angle = random.uniform(0, 2 * math.pi)

    # Random distance in miles
    distance = random.uniform(min_distance, max_distance)

    # New coordinates based on random distance and angle
    delta_lat = distance / earth_radius
    delta_lng = distance / earth_radius / math.cos(deg2rad(base_lat))

    new_lat = base_lat + rad2deg(delta_lat)
    new_lng = base_lng + rad2deg(delta_lng)

    return new_lat, new_lng

# 쓰레드에서 실행될 함수
def thread_function(thread_id, lat, lng, min_dist, max_dist):
    while True:
        # 위치 업데이트 (10 miles/h로 이동)
        delta_lat = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)
        delta_lng = random.uniform(-MOVEMENT_SPEED, MOVEMENT_SPEED)

        lat += delta_lat
        lng += delta_lng

        # API에 위치 전송
        payload = {
            "parent": thread_id,
            "type": "Driver",
            "location": {
                "lat": str(lat),
                "lng": str(lng)
            }
        }
        print("payload", payload)
        try:
            print(BASE_URL)
            response = requests.post(BASE_URL, json=payload)
            if response.status_code == 200:
                print(f"Thread {thread_id}: Location sent successfully!")
            else:
                print(f"Thread {thread_id}: Failed to send location.")
                print(response.text)
                
        except Exception as e:
            print(f"Thread {thread_id}: Error sending location - {e}")

        # 1초마다 위치 갱신
        time.sleep(5)

# 쓰레드 시작 함수
def start_threads():
    threads = []
    
    # 첫 번째 5개의 쓰레드는 5마일 범위 내에서 위치 설정
    for i in range(5):
        lat, lng = random_location(START_LAT, START_LNG, 0, 5)  # 5마일 범위 내
        thread = threading.Thread(target=thread_function, args=(i + 1, lat, lng, 0, 5))
        thread.daemon = True  # 데몬 쓰레드로 설정
        threads.append(thread)
        thread.start()

    # 나머지 5개의 쓰레드는 5마일~10마일 범위 내에서 위치 설정
    for i in range(5, 10):
        lat, lng = random_location(START_LAT, START_LNG, 5, 10)  # 5-10마일 범위 내
        thread = threading.Thread(target=thread_function, args=(i + 1, lat, lng, 5, 10))
        thread.daemon = True  # 데몬 쓰레드로 설정
        threads.append(thread)
        thread.start()

    return threads

# 메뉴 출력 함수
def show_menu():
    print("1. 시작")
    print("2. 종료")
    choice = input("메뉴를 선택하세요: ")
    return choice

# 종료 시그널 처리 함수
def signal_handler(sig, frame):
    print("\n프로그램을 종료합니다.")
    sys.exit(0)  # 프로그램 종료

# 메인 함수
def main():
    signal.signal(signal.SIGINT, signal_handler)  # Ctrl+C 시그널 처리
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            threads = start_threads()
            print("쓰레드가 시작되었습니다.")
            try:
                while True:
                    time.sleep(1)  # 쓰레드가 계속 동작할 수 있도록 대기
            except KeyboardInterrupt:
                print("\n중지되었습니다.")
                break

        elif choice == "2":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다.")

if __name__ == "__main__":
    main()