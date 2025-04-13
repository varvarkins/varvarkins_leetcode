# remove_spaces("kot     sobaka") -> "kot sobaka"
#  a b
#    ^
#     ^          
def remove_spaces(s : str):
    s = list(s)
    l = 0
    r = 0

    while r < len(s) and s[r] == ' ':
        r += 1
    while r < len(s):
        while r < len(s) and s[r] != ' ':
            s[l] = s[r]
            r += 1
            l += 1
        if r < len(s) and s[r] == ' ':
            s[l] = s[r]
            r += 1
            l += 1
        while r < len(s) and s[r] == ' ':
            r += 1

    res = ''.join(s[:l])
    if len(res) > 0 and res[len(res) - 1] == ' ':
        res = res[:-1]
    return res

s = remove_spaces('   ')
print(s, len(s))
                #      ^
                #        ^  
