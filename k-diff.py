class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = []
        maps = {}
        for s in nums:
            if s in maps:
                res.append((maps[s],s))          
            maps[s+k] = s
        return len(set(res))
