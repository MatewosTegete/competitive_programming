class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i - count] = nums[i]
            else:
                count += 1
        for i in range(len(nums) - count, len(nums)):
            nums[i] = 0
