class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        our_sum = 0
        prefixSums = {0: 1}

        for n in nums:
            our_sum += n
            diff = our_sum - k

            res += prefixSums.get(diff, 0)
            prefixSums[our_sum] = 1 + prefixSums.get(our_sum, 0)

        return res
