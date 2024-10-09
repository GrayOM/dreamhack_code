class STREAM:
    def __init__(self, seed, size):
        self.state = self.num2bits(seed, size)

    def num2bits(self, num, size):
        assert num < (1 << size)
        return bin(num)[2:].zfill(size)
    
    def bits2num(self, bits):
        return int('0b' + bits, 2)
    
    def shift(self):
        new_bit = self.state[-1]
        self.state = new_bit + self.state[:-1]
        return new_bit
    
    def getNbits(self, num):
        sequence = ""
        for _ in range(num):
            sequence += self.shift()
        return sequence

    def encrypt(self, plaintext):
        ciphertext = b""
        for p in plaintext:
            stream = self.bits2num(self.getNbits(8))
            c = p ^ stream
            ciphertext += bytes([c])
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = b""
        for c in ciphertext:
            stream = self.bits2num(self.getNbits(8))
            p = c ^ stream
            plaintext += bytes([p])
        return plaintext


if __name__ == "__main__":
    import os

    # 테스트: Alice와 Bob이 같은 seed로 암호화와 복호화를 하는 경우
    for seed in range(0x100):
        Alice = STREAM(seed, 16)
        Bob = STREAM(seed, 16)
        plaintext = os.urandom(128)
        ciphertext = Alice.encrypt(plaintext)
        assert plaintext == Bob.decrypt(ciphertext)

    # 제공된 암호문 복호화
    ciphertext = bytes.fromhex("3cef03c64ac240c349971d9e4c951cc14ec4199f409249c21e964ac540c540944f901c934cc240934d96419f4b9e4d9f1cc41dc61dc34e9219c31bc11a914f9141c61ada")

    # 모든 seed 값을 시도하여 복호화
    for seed in range(0x100):
        Bob = STREAM(seed, 16)
        plaintext = Bob.decrypt(ciphertext)
        
        # 바이트 형태로 평문 출력
        print(f"Seed: {seed}, Plaintext (bytes): {plaintext}")
        
        # UTF-8로 디코딩 가능한지 시도
        try:
            print(f"Seed: {seed}, Plaintext (decoded): {plaintext.decode()}")
        except UnicodeDecodeError:
            # UTF-8 디코딩이 불가능하면 넘어감
            pass
