class Solution:
    def romanToInt(self, s: str) -> int:
        order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = {'I': (1, ''), 'V': (5, 'I'), 'X': (10, 'I'), 'L': (50, 'X'), 'C': (100, 'X'), 'D': (500, 'C'), 'M': (1000, 'C')}
        result = values[ s[0] ][0]
        for i in range(1, len(s)):
            if s[i-1] == values[ s[i] ][1]:
                result -= values[ values[ s[i] ][1] ][0]
                temp = values[ s[i] ][0] - values[ values[ s[i] ][1] ][0]
                result += temp
            else:
                result += values[ s[i] ][0]
                
        return result
