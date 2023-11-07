class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        curr_sum = 0
        i = 0
        while i < len(nums):
            curr_sum += nums[i]
            res.append(curr_sum)
            i += 1
        return res
