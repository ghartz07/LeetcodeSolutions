from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            temp = nums.pop(0)
            res.append(reduce(mul,nums))
            nums.append(temp)

        return res