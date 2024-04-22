class Solution(object):
    def reverse(self, x):
        revX = str(x)[::-1]
        negativeFlag = 0
        #check for negative
        if(str(x)[0] == '-'):
            revX = revX.rstrip('-')
            negativeFlag = 1
        if(int(revX) > 2**31-1):
            return 0
        else:
            if(negativeFlag == 1):
                return int(revX) * -1
            return int(revX)
        