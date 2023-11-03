class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        res = ""

        while l < len(word1) and r < len(word2):
            if word1[l:] >= word2[r:]:
                res += word1[l]
                l += 1
            else:
                res += word2[r]
                r += 1

        res += word1[l:] + word2[r:]

        return res
