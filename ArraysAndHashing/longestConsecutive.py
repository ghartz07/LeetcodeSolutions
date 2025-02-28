class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        if not nums:
            return 0

        counter, counter_max = 1, 1

        prev_item = nums.pop(0)
        for cur_item in nums:
            if ((prev_item + 1) == cur_item):
                counter += 1
            elif((prev_item + 1) > cur_item):
                continue
            else:
                if (counter_max < counter):
                    counter_max = counter
                counter = 1

            prev_item = cur_item

        if (counter_max < counter):
            counter_max = counter

        return counter_max