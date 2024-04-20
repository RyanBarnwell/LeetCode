class Solution(object):
    def lengthOfLastWord(self, s):
        lis = s.split()
        return len(lis[len(lis)-1])