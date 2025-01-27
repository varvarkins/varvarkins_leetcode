def two_Sums(arr, target):
    dict_of_curr_nums = {}
    for i in range (0, len(arr)):
        compliment = target - arr[i]
        if compliment in dict_of_curr_nums:
            return dict_of_curr_nums[compliment], i
        dict_of_curr_nums[arr[i]] = i
    return False
arr = [1, 1, 5, 7]
target = 6
print(two_Sums(arr, target))