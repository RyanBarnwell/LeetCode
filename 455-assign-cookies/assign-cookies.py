class Solution(object):
    def findContentChildren(self, g, s):
        #assign smallest first
        s.sort()
        g.sort()
        cCount = 0
        for x in range(0, len(s)):
            if(s[x] >= g[cCount]):
                cCount = cCount+1
            if(cCount == len(g)):
                break
        return cCount
            