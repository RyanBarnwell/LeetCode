import numpy as np

class Solution(object):
    def firstMissingPositive(self, nums):
        nums = np.array(nums)
        #get all positive
        nums = nums[nums>0]
        nums = list(set(nums))
        nums.sort()
        
        if(len(nums) == 0):
            return 1
        
        for x in range(1, len(nums)+1):
            if(nums[x-1] != x):
                return x
        return x+1
        