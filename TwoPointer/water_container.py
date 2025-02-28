class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pt1 = 0
        pt2 = len(heights)-1
        max_area = 0

        while (pt1 < pt2):
            width = pt2 - pt1
            area = (min(heights[pt1], heights[pt2]) * width)

            if (area > max_area):
                max_area = area

            if(heights[pt1] < heights[pt2]):
                pt1 +=1
            else:
                pt2 -=1



        return max_area