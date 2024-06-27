import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i,j=0,0
        min_len=math.inf
        win_sum=0
        
        for j in range(len(nums)):
            win_sum+=nums[j]
            while(win_sum>=target):
                win_sum-=nums[i]
                min_len = min(min_len, j-i+1)
                i+=1
        
        if(min_len == math.inf):
            return 0
        return min_len
                
            
        