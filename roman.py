class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        check = 0
        for i in range(len(s)):
            current = values[s[i]]
            if  current > check:
                result += current - 2*check
            else:
                result += current
            check = current
        return result