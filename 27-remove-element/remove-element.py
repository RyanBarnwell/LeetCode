class Solution(object):
    def removeElement(self, nums, val):
        x = 0
        length = len(nums)
        while(x <= length):
            if(val in nums):
                nums.pop(nums.index(val))
            x += 1
        return len(nums)
        