class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        bucket_count = len(nums) + 1
        buckets = [[] for _ in range(bucket_count)]

        for num, freq in counts.items():
            buckets[freq].append(num)


        buffer = []
        for bucket in reversed(buckets):
            for num in bucket:
                buffer.append(num)
                if len(buffer) == k:
                    return buffer
        return buffer