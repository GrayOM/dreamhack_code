import requests
import json
import time

# 쿠폰 발급 요청 함수
def claim_coupon(authorization):
    url = "http://host3.dreamhack.games:24304/coupon/claim"  # 쿠폰 발급 경로 설정

    headers = {
        "Authorization": authorization  # Authorization 헤더에 세션 ID를 넣어줍니다.
    }

    # 쿠폰 발급 요청 보내기
    response = requests.get(url, headers=headers)
    
    # 요청에 대한 응답을 확인하고 출력
    if response.status_code == 200:
        coupon = json.loads(response.text).get("coupon")
        print("쿠폰 발급 성공:", coupon)
        return coupon  # 발급받은 쿠폰 반환
    else:
        print("쿠폰 발급 실패:", response.status_code, response.text)
        return None  # 실패 시 None 반환

# 쿠폰 제출 요청 함수
def submit_coupon(authorization, coupon, start_time):
    url = "http://host3.dreamhack.games:24304/coupon/submit"  # 쿠폰 제출 경로 설정

    headers = {
        "Authorization": authorization,  # Authorization 헤더
        "coupon": coupon  # 발급받은 쿠폰
    }

    # 쿠폰 제출 요청 보내기
    response = requests.get(url, headers=headers)
    
    # 요청에 대한 응답을 확인하고 출력
    elapsed_time = time.time() - start_time  # 요청이 시작된 이후 경과된 시간 계산
    print(f"Elapsed Time: {elapsed_time:.2f} seconds - 쿠폰 제출 요청: {response.status_code}, {response.text}")

def submit_time60(authorization):
    # 쿠폰 발급 받기
    coupon = claim_coupon(authorization)
    
    if coupon is not None:
        # 60초 동안 1초 간격으로 쿠폰을 제출하는 작업
        start_time = time.time()  # 시작 시간을 기록
        for _ in range(60):  # 60번 반복 (1초 간격으로 요청)
            submit_coupon(authorization, coupon, start_time)  # 쿠폰 제출
            time.sleep(1)  # 1초 간격으로 제출


# 쿠폰을 발급받고 첫 제출 및 45초~46초 사이에 한 번 더 제출하는 함수
def claim_and_submit_coupon(authorization):
    # 쿠폰 발급 받기
    coupon = claim_coupon(authorization)
    
    if coupon is not None:
        # 발급받은 쿠폰과 시작 시간
        start_time = time.time()  # 시작 시간을 기록
        
        # 첫 번째 제출
        submit_coupon(authorization, coupon, start_time)
        
        # 45초에서 46초 사이에 제출하도록 설정
        while True:
            current_time = time.time() - start_time
            if 45 <= current_time <= 46:  # 45초에서 46초 사이에 요청
                submit_coupon(authorization, coupon, start_time)
                break
            time.sleep(0.1)  # 계속해서 확인하면서 대기

# 예시로 사용될 Authorization 값
authorization = "e2f1d21d3c1d473ba7e5526673570f44"  # 실제 Authorization 값으로 교체

# 쿠폰 발급 및 제출 시작
claim_and_submit_coupon(authorization)