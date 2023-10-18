class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        l, r = 0, len(piles) - 1
        while l < r:
            sum += piles[r-1]
            l += 1
            r -= 2
        return sum
