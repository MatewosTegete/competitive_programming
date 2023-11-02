class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_copy = nums[:]
        for i in range(len(nums_copy) - 1):
            if nums_copy[i + 1] == nums_copy[i]:
                nums.remove(nums_copy[i + 1])
        return len(nums)
