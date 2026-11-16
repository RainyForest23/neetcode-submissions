# value appears just more than once -> just compare then if a same number appear -> TRUE
# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#                 else:
#                     continue
#         return False

# check with blank set -> if value is not in set
# -> add a value -> iterate this process
# -> finally return False
class Solution: # set으로 O(n)
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # set()은 중복허용하지않는집합
        for num in nums:
            if num not in seen:
                seen.add(num)
            # if seen(num) in nums:
            else:
                return True
                # else: 없어도 된다.
                #     continue
        return False


            
    

        