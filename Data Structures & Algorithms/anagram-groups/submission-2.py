# regard each vocab as one char
# have to use sublists
# use "sorted()" -> 순서 통일하여 char List 반환

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = {}
#         for item in strs:
#             key = "".join(sorted(item))
        
#             if key not in groups:
#                 groups[key] = [] # first, make empty list
#                 groups[key].append(item)
#             # if sorted(item) not in groups:
#             # result of "sorted()" is List. 
#             else:
#                 groups[key].append(item)
#         return list(groups.values())

# Optimization
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            key = "".join(sorted(item))
        
            if key not in groups:
                groups[key] = [] # first, make empty list
            groups[key].append(item)
            # else:
            #     groups[key].append(item)
            # 중복되는건 굳이 else로 한번 더 쓸 이유 없음. 
        return list(groups.values())

# return groups -> 
# {"act": ["act", "cat"], "opst": ["pots", "tops", "stop"], "aht": ["hat"]}

# 여기서 values 만 꺼내는게 ".values()"
# 이걸 다시 list로 묶는게 list()

# sorted() : 정렬 -> list 반환
# sorted("cat")            # ['a', 'c', 't'] 
# .join() : list 원소들을 . 앞의 문자열로 이어 붙임
# "".join(sorted("cat"))   # 'act'



        
        