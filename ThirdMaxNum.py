class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(dict.fromkeys(nums))
        len_1 = len(nums)
        nums.sort()
        if (len_1<3):
            return nums[-1]
        else:
            first = nums[0]
            second = -sys.maxsize
            third = -sys.maxsize 
            for i in range(1,len_1):
                if (nums[i]>first):
                    first = nums[i]
            for i in range(0, len_1): 
                if (nums[i] > second and 
                    nums[i] < first): 
                    second = nums[i]
            third = -sys.maxsize 
            for i in range(0, len_1):
                if (nums[i] > third and nums[i] < second): 
                    third = nums[i]
            return third
