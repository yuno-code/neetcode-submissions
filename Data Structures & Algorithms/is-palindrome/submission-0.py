class Solution:
    def isPalindrome(self, s: str) -> bool:
        strip_text = "".join(filter(str.isalnum, s)).lower()
        r = len(strip_text) - 1
        for i in range(len(strip_text)):
            if strip_text[i] != strip_text[r - i]:
                return False

            # if i != x:
            #     return False

        return True