class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if s == '':
            return 0
        
        chars = set([s[0]])
        long = 1
        left = 0
        next_left = 0
        right = 1
        while right < len(s):
            if s[right] not in chars:
                chars = {s[next_left], s[right]}
                left = next_left
            
            if s[next_left] != s[right]:
                next_left = right
            new = right-left+1
            if new > long:
                long = new
            
            right += 1
            
        return long
