# remove_spaces("kal     sobaki") -> "kal sobaki"
#  a b
#    ^
#     ^          
def remove_spaces_around(s : str):
    s = list(s)
    l = 0
    r = 0
    while r < len(s) and s[r] == ' ':
        r += 1
    l = r
    r = len(s) - 1
    while r > l and s[r] == ' ':
        r -= 1
    return ''.join(s[l: r + 1]), len(s), l, r

print(remove_spaces_around('  a  j h u    '))