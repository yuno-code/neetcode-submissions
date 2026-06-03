class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        best = 0
        for i, n in enumerate(s):
            if n in seen and seen[n] >= start:
                start = seen[n] + 1
            seen[n] = i
            best = max(best, i - start + 1)
        return best