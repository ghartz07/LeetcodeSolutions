class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        res = []
        bucket = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        for num, freq in count_dict.items():
            bucket[freq].append(num)

        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res