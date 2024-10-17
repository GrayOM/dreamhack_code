# byte_140003000 배열을 정의합니다.
byte_140003000 = [
    0xAC, 0xF3, 0x0C, 0x25, 0xA3, 0x10, 0xB7, 0x25, 0x16, 0xC6,
    0xB7, 0xBC, 0x07, 0x25, 0x02, 0xD5, 0xC6, 0x11, 0x07, 0xC5,
    0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C
]

# a1[i] 값을 브루트 포스로 찾습니다.
for i in range(0,0x15):
    for possible_a1 in range(256):  # 0부터 255까지 시도
        result = (-5 * possible_a1) % 256  # 수식: -5 * possible_a1 연산 후, 256으로 나눈 나머지 처리 (8-bit unsigned wraparound)
        if result == byte_140003000[i]:
            # 문자열로 출력하는 부분 수정
            print(f"{chr(possible_a1)}", end='')
