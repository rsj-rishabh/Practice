class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        result = []
        
        if len(nums) == 0:
            if upper == lower:
                return [str(upper)]
            else:
                return [str(lower)+'->'+str(upper)]
        
        if (nums[0] - lower) >= 1:
            result.append([lower, nums[0]-1])
        
        if len(nums) > 1:
            for i in range(1, len(nums)):
                if (nums[i] - nums[i-1]) > 1:
                    result.append([nums[i-1]+1, nums[i]-1])
        
        if (upper - nums[-1]) >= 1:
            result.append([nums[-1]+1, upper])
            
        for i in range(len(result)):
            up = result[i][1]
            low = result[i][0]
            if up == low:
                result[i] = str(up)
            else:
                result[i] = str(low) + '->' + str(up)
            
        return result
