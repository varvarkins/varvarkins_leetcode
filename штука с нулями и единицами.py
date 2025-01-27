def longestOnes(nums: list[int], k: int) -> int:
        zero_cnt = 0
        l = 0
        r = 0 
        res = 0
        while r < len(nums):
            while r < len(nums) and nums[r] != 0:
                r += 1

            res = max(r - l - zero_cnt, res)
            if r < len(nums) and zero_cnt < k:
                r += 1
                zero_cnt += 1
            elif r < len(nums) and zero_cnt >= k:
                if nums[l] == 0:
                    zero_cnt -= 1
                l += 1
            res = max(r - l - zero_cnt, res)


        return res


# nums = [0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
#       ^
#       ^       
#nums = [1]
# nums = [0]
# nums = [0, 1]
# nums = [1, 0]
# nums = [1, 0, 1]
# nums = [0, 1, 0]
#k = 2
nums = [1, 1, 1, 0, 1, 0]
k =  1 
print (longestOnes(nums, k))

