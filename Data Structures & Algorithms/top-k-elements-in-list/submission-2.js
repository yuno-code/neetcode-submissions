class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const counts = {};

        for (const num of nums) {
            counts[num] = (counts[num] || 0) + 1;
        }

        const bucketCount = nums.length + 1;
        const buckets = Array.from({ length: bucketCount }, () => []);

        for (const [num, freq] of Object.entries(counts)) {
            buckets[freq].push(Number(num));
        }

        const buffer = [];
        for (let i = buckets.length - 1; i >= 0; i--) {
            for (const num of buckets[i]) {
                buffer.push(num);
                if (buffer.length === k) {
                    return buffer;
                }
            }
        }
        return buffer;
    }
}