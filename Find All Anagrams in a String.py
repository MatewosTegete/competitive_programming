class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = Counter(p)
        window_counter = Counter(s[:len(p)])
        if window_counter == p_counter:
            result.append(0)
        for i in range(1, len(s) - len(p) + 1):
            window_counter[s[i-1]] -= 1
            if window_counter[s[i-1]] == 0:
                del window_counter[s[i-1]]
            window_counter[s[i+len(p)-1]] += 1
            if window_counter == p_counter:
                result.append(i)
        return result
