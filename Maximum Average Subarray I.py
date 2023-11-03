from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l, r = 0, k-1
        sum1 = sum(nums[l:r+1])
        array = [sum1]

        while r < len(nums) - 1:
            sum1 -= nums[l]
            l += 1
            r += 1
            sum1 += nums[r]
            array.append(sum1)

        max_sum = max(array)
        avg = max_sum / k
        return avg
