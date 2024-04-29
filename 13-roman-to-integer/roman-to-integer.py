class Solution(object):
    def romanToInt(self, s):
        romeDict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        rsum = 0
        lastRome = 0
        revRome = s[::-1]
        for x in revRome:
            rome = romeDict.get(x)
            if(rome < lastRome):
                rsum = rsum - rome
            else:
                rsum = rsum + rome
            lastRome = rome
        return rsum