class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        pt1 = 0
        pt2 = len(numbers)-1

        while (pt1 < pt2):
            sum_ = numbers[pt1] + numbers[pt2]
            if(sum_ < target):
                pt1 += 1
            elif(sum_ > target):
                pt2 -= 1
            else:
                return [pt1+1, pt2+1]