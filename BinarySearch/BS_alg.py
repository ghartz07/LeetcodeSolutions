class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left > right:
                return -1
            
            middle = (left + right) // 2
            
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                return binary_search(nums, target, middle + 1, right)
            else:
                return binary_search(nums, target, left, middle - 1)
        
        return binary_search(nums, target, 0, len(nums) - 1)