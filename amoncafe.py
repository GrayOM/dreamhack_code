def reverse():
    # 인코딩된 문자열을 지정
    encoded_str = "1_c_3_c_0__ff_3e"
    
    # 최종 결과 값을 저장할 변수 초기화
    result = 0
    
    # shift_amount는 비트 이동량을 추적하며, 처음에는 15로 설정
    shift_amount = 15

    # encoded_str의 각 문자를 반복하면서 처리
    for char in encoded_str:
        # '_' 문자는 특별한 값으로 처리. 0xb (11 in decimal)로 설정
        if char == '_':
            value = 0xb
        # 'c', 'd', 'e', 'f' 문자들은 각각 16진수 값으로 변환
        elif char in 'cdef':
            value = int(char, 16)  # 16진수로 변환
        # 숫자 문자는 그대로 10진수 값으로 변환
        else:
            value = int(char)

        # result 변수에 비트 이동하여 값을 추가
        # (value << (shift_amount * 4))는 value를 4배씩 이동시키는 역할을 함
        result |= (value << (shift_amount * 4))
        
        # 다음 문자를 처리할 때 이동할 비트 크기를 1만큼 감소
        shift_amount -= 1

    # 결과 출력
    print(result)

# 함수 호출
reverse()
