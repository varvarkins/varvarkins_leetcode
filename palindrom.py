#a = 'шалаш'
def is_palindrom(word):
    word = list(word)
    l = 0
    r = len(word) - 1
    while l < r:
        if word[l] == word[r]:
            l += 1
            r -= 1
        else:
            return False
    return True

print(is_palindrom(''))