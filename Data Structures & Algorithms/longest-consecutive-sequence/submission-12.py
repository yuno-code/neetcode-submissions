class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        count = 0
        best = 0
        for n in mySet:
            count = 0
            if n-1 not in mySet:
                count = 1
                while n + count in mySet:
                    print(f"n+ count is: {n+count}")
                    count += 1
                best = max(best, count)
        return best