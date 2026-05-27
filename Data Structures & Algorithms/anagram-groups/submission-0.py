class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            val = "".join(sorted(s))
            if val not in result:
                result[val] = []
            result[val].append(s)

        print(result)
        return list(result.values())