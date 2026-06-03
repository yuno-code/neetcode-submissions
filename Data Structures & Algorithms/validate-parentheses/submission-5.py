class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        brackets = {'(':')', '{':'}', '[':']'}
        seen = []

        for n in s:
            if n in brackets:
                seen.append(n)
            else:
                if len(seen) == 0:
                    return False
                x = seen.pop()
                if brackets[x] != n:
                    return False
        if len(seen) == 0:
            return True
        else:
            return False