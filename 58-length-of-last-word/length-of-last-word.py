class Solution(object):
    def lengthOfLastWord(self, s):
        lis = s.split()
        word = lis[len(lis)-1]
        return len(word)