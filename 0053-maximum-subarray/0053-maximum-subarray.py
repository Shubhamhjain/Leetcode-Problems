import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        i,j=0,0
        max_sum = -math.inf
        win_sum=0
        
        for j in range(len(nums)):
            win_sum+=nums[j]
            max_sum = max(max_sum, win_sum)
            if win_sum<0:
                win_sum=0
            
            
            
        if(len(nums)==1):
            return nums[0]
        
        return max_sum
            
        