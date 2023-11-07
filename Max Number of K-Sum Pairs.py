class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        operations = 0

        for num in counter:
            complement = k - num
            if complement in counter:
                pairs = min(counter[num], counter[complement])
                if num == complement:
                    pairs //= 2
                operations += pairs
                counter[num] -= pairs
                counter[complement] -= pairs

        return operations
