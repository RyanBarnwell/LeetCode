class Solution(object):
    def mySqrt(self, x):
        count = 0
        start = 1
        while True:
            if(x-start < 0):
                return count
            x = x-start
            count = count + 1
            start = start + 2
        