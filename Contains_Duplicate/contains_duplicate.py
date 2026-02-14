from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #same concept as 2 sum
        seen = {}
        for v in nums:
            if v in seen:
                return True
            seen[v] = v
        return False
