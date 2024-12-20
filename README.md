# AES 암호화 구현

이 프로젝트는 AES 암호화 알고리즘을 Python으로 구현한 것입니다. AES는 다양한 암호화 모드(ECB, CBC, CFB, OFB, CTR)를 지원하며, 각 모드는 특정 용도에 맞게 데이터를 암호화하는 방법을 제공합니다.

## 주요 기능

- **AES 암호화**: AES 알고리즘의 키 확장, SubBytes, ShiftRows, MixColumns, AddRoundKey 등 주요 연산을 구현.
- **암호화 모드**: ECB, CBC, CFB, OFB, CTR 모드 지원.
- **패딩**: 16바이트 크기의 블록으로 맞추기 위한 패딩 처리.
- **랜덤 초기화 벡터(IV) 생성**: CBC, CFB, CTR 모드에서 사용되는 초기화 벡터를 랜덤으로 생성.

## AES 연산 설명

1. **키 확장**: 128비트 키를 11개의 라운드 키로 확장.
2. **SubBytes**: 각 바이트를 S-box를 이용해 대체.
3. **ShiftRows**: 각 행을 순차적으로 이동.
4. **MixColumns**: 각 열을 고정된 다항식을 사용해 섞기.
5. **AddRoundKey**: 라운드 키와 XOR 연산.
6. **AES 모드**: ECB, CBC, CFB, OFB, CTR 등 여러 암호화 모드 지원.

## 암호화 모드

- **ECB (Electronic Codebook)**: 각 블록을 독립적으로 암호화.
- **CBC (Cipher Block Chaining)**: 이전 암호문과 XOR 연산 후 암호화.
- **CFB (Cipher Feedback)**: 이전 암호문을 다음 입력으로 사용.
- **OFB (Output Feedback)**: IV를 암호화하여 스트림을 생성하고 XOR 연산.
- **CTR (Counter Mode)**: 카운터 값을 암호화하여 스트림 생성 후 XOR 연산.

## 사용 방법

1. Python 환경에서 `AES.py` 파일을 실행하면, 암호화 과정을 확인할 수 있습니다.
2. `block`과 `key` 변수를 변경하여 다른 데이터를 테스트할 수 있습니다.

### 예시 사용법

```python
# 예시 키와 블록
key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 
       0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c]
block = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 
         0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]

# 상태로 변환
state = block2state(block)
key_state = block2state(key)

# AES 암호화
ciphertext = AES_ENC(state, key_state)

# 결과 출력
print("암호문:")
hex_print(ciphertext)
