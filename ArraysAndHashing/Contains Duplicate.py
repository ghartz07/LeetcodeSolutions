class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        return not(len(temp) == len(nums))