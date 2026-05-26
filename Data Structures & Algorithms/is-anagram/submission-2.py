class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        first = "".join(sorted(s))
        second = "".join(sorted(t))
        if first == second:
            return True
        
        return False