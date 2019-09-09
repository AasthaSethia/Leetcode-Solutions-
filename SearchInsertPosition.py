    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        position = 0
        for i in range(length):
            if (nums[i] == target):
                position = nums.index(target)
            else:
                nums.append(target)
                nums.sort()
                position = nums.index(target)
        return position 
