def threeSum(nums: list[int]):
    nums.sort()
    ans = []
    for i in range (len(nums)):
        if i > 0 and nums[i] == nums [i - 1]:
            continue
        target = -nums[i]
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if nums[l] + nums[r] == target:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
    return ans             

print(threeSum([-2, 3, 1, 7, -4, 9]))