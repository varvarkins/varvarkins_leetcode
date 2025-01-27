def hex_to_decimal(varvara : chr):
    if '0' <= varvara <= '9':
        return ord(varvara) - ord('0')
    return 10 + ord(varvara) - ord('A')

def decimal_to_hex(varvara : int):
    if 0 <= varvara <= 9:
        return chr(ord('0') + varvara)
    return chr(varvara - 10 + ord('A'))

def get_idx(s: str, idx: int) -> chr:
    if len(s) - 1 - idx < 0:
        return '0'
    return s[len(s) - 1 - idx]

def add_two_hex_numbers(a : str, b : str) -> str:
    i = 0
    carry = 0
    res = []

    while i != max(len(a), len(b)):
        sum_ = hex_to_decimal(get_idx(a, i)) + hex_to_decimal(get_idx(b, i)) + carry
        i += 1
        res.append(decimal_to_hex(sum_ % 16)) 
        carry = sum_ // 16

    if carry != 0:
        res.append(decimal_to_hex(carry))

    return ''.join(res[::-1])

print(add_two_hex_numbers('8AB', 'B228'))
