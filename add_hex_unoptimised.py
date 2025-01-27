# a - {-inf; +inf}, b - {-inf; +inf}
def hex_to_decimal(varvara : chr):
    if '0' <= varvara <= '9':
        return ord(varvara) - ord('0')
    return 10 + ord(varvara) - ord('A')

def decimal_to_hex(varvara : int):
    if 0 <= varvara <= 9:
        return chr(ord('0') + varvara)
    return chr(varvara - 10 + ord('A'))
# add_two_hex_numbers('8AB', 'B228') == 'BAD3'
# 123 + 19 
#  2 + 3
# F 1

def add_two_hex_numbers(a : str, b : str) -> str:
    i = len(a) - 1 
    j = len(b) - 1
    carry = 0
    res = []
    while min(i, j) != -1:
        sum_ = hex_to_decimal(a[i]) + hex_to_decimal(b[j]) + carry
        i -= 1
        j -= 1
        res.append(decimal_to_hex(sum_ % 16)) 
        carry = sum_ // 16

    while i != -1:
        sum_ = hex_to_decimal(a[i]) + carry
        i -= 1
        res.append(decimal_to_hex(sum_ % 16))
        carry = sum_ // 16

    while j != -1:
        sum_ = hex_to_decimal(b[j]) + carry
        j -= 1
        res.append(decimal_to_hex(sum_ % 16))
        carry = sum_ // 16

    if carry != 0:
        res.append(decimal_to_hex(carry))

    return res[::-1]
# a = 14 b = A11C
print("".join(add_two_hex_numbers("14", "A11C")))
