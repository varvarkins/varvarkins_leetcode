
# Даны два отсортированных массива надо вернуть элементы которые встречаются в левом и не встречаются в правом
# foo([1, 3, 5, 7], [0, 1, 2, 7, 9]) -> [3, 5]
#      ^      
#         ^
#                             ^

# foo([1, 3, 5, 7], [0, 2, 6, 9]) -> [3, 5]
#      ^      
#      ^
#                    ^

# foo([1, 3, 5, 7], [1, 3, 5, 7]) -> [3, 5]
#      ^      
#      ^
#                    ^


# foo([1, 3, 5, 7], [1, 2, 3]) -> [3, 5]
#      ^      
#      ^
#                    ^

# foo([1, 3, 5, 7], [0, 7, 9]) -> [1, 3, 5]
#      ^      
#      ^
#                       ^

# foo([2, 7, 8], [2, 5])
#      ^
#         ^ 
#                       ^
# foo([1, 2, 10, 13, 15, 17], [0, 7, 9]) -> [1, 3, 5]
#             ^      
#             ^
#                                 ^


def elements_which_exist_in_left_but_doesnt_exist_in_right(a, b):
    l_reader = 0
    l_writer = 0
    r = 0
    while l_reader < len(a) and r < len(b):
        while l_reader < len(a) and r < len(b) and a[l_reader] > b[r]:
            r += 1
        while l_reader < len(a) and r < len(b) and a[l_reader] == b[r]:
            r += 1
            l_reader += 1
        while l_reader < len(a) and r < len(b) and a[l_reader] < b[r]:
            a[l_writer] = a[l_reader]
            l_reader += 1
            l_writer += 1

    while l_reader < len(a):
        a[l_writer]= a[l_reader]
        l_reader += 1
        l_writer += 1

    return a[:l_writer]



