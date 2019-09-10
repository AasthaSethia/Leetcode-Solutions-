class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        len_1 = len(nums)
        if len_1 == 1 or len_1 ==0 :
            return True 
        p = None
        for i in range(len_1-1):
            if nums[i]> nums[i+1]:
                if p is not None:
                    return False 
                p = i 
        return(p is None or p == 0 or p == len_1-2 or nums[p-1]<= nums[p+1] or nums[p]<= nums[p+2])
                
        
