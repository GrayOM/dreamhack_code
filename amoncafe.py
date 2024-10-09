def reverse():
    encoded_str = "1_c_3_c_0__ff_3e"
    result = 0
    shift_amount = 15

    for char in encoded_str:
        if char == '_':
            value = 0xb
        elif char in 'cdef':
            value = int(char, 16)
        else:
            value = int(char)

        result |= (value << (shift_amount * 4))
        shift_amount -= 1

    print(result)

reverse()
