# one pair of indices is guaranteed.
# to find out smaller indices,
# define target - first_index -> find in nums
# iterate this process
# two comparable value is need so time complextity would be O(n^2)

class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     solution = []
    #     for i in range(len(nums)): 
    #         # not only value but also indices is need when to get a return value
    #         f = target - nums[i]
    #         for j in range(i+1, len(nums)):
    #             if f == nums[j]:
    #                 solution.append(i)
    #                 solution.append(j)
    #                 return solution
                    # return i, j 
                    # expected return value is List
                    # so we have to define another List

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using {} -> record pair already seen before
        seen = {}
        for i, num in enumerate(nums): # index와 value 모두 필요할 때 enumerate
            pair = target - num # 0 3 -> pair=4 // 1 4 -> pair = 3
            if pair in seen:
                return [seen[pair], i]
            seen[num] = i # 3: 0

                            



        