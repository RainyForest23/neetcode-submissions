# start : 21:22

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_sort = sorted(set(nums)) # -2,1,2,3,5,6
        
        x = 1

        while x in nums_sort:
            x += 1
        return x
