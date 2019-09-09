class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort()
        count =0
        for i in nums: 
            if (i == val):
                count = count +1
        for i in range(count):
            nums.remove(val)
        length = len(nums)
        return length
