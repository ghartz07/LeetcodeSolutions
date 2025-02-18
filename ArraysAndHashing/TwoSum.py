class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pt1 = 0
        pt2 = len(nums) - 1

        nums_dict = {i: value for i,value in enumerate(nums)}
        nums_sorted = list(sorted(nums_dict.items(), key=lambda item: item[1]))

        for i in range(len(nums_sorted)):
            sum = nums_sorted[pt1][1] + nums_sorted[pt2][1]
            if (sum == target):
                if (nums_sorted[pt1][0] < nums_sorted[pt2][0]):
                    return [nums_sorted[pt1][0], nums_sorted[pt2][0]]
                else:
                    return [nums_sorted[pt2][0], nums_sorted[pt1][0]]
            elif (sum < target):
                pt1 += 1
            else:
                pt2 -= 1

        return 0
