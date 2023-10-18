class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums
        l, r = 0, 1
        while l < r and r < len(nums):
            if nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
            r += 1
            if r < len(nums) and nums[l] > nums[r]:
                nums[l], nums[r] = nums[r], nums[l]

            if l < r and r == len(nums) - 1:
                l += 1
                r = l + 1

        return nums
