class Solution(object):
    def firstMissingPositive(self, nums):
        length = len(nums)
        #swap positive values to end of array
        #pseudo-sort
        pos = 0
        for i in range(0, length):
            if nums[i] <= 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        #pos is negative index
        #cut array at negative index
        nums = nums[pos:]
        
        if not nums:
            return 1
        
        for i in range(0, len(nums)):
            # check if number is at expected index and if it has been accessed
            #removes need to remove duplicates
            if(abs(nums[i]) - 1 < len(nums) and nums[abs(nums[i]) - 1] > 0):
                #sets index to negative to mark indexing
                nums[abs(nums[i]) - 1] = -nums[abs(nums[i]) - 1]

        #use len to get current length
        for i in range(0, len(nums)):
            #return first index
            if nums[i] > 0:
                return i + 1

        return len(nums) + 1
        