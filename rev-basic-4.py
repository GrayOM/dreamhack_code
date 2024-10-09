byte_7FF793503000 = [
    0x24, 0x27, 0x13, 0xC6, 0xC6, 0x13, 0x16, 0xE6, 0x47, 0xF5,  # 첫 번째 라인
    0x26, 0x96, 0x47, 0xF5, 0x46, 0x27, 0x13, 0x26, 0x26, 0xC6,  # 두 번째 라인
    0x56, 0xF5, 0xC3, 0xC3, 0xF5, 0xE3, 0xE3
]

# 변환 및 비교
for i in range(len(byte_7FF793503000)):  
    # cp949 가 뜨면 & 0xF0 을 넣고 아니면 & 0xF0 을 지우세요 계산 결과는 같을겁니다.
    print(chr((16 * byte_7FF793503000[i]) & 0xF0 | (byte_7FF793503000[i] >> 4)), end='')
