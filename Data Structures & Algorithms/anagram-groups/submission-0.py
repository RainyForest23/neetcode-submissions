# regard each vocab as one char
# have to use sublists
# use "sorted()" -> 순서 통일하여 char List 반환

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for item in strs:
            key = "".join(sorted(item))
        
            if key not in groups:
                groups[key] = [] # first, make empty list
                groups[key].append(item)
            # if sorted(item) not in groups:
            # result of "sorted()" is List. 
            else:
                groups[key].append(item)
        return list(groups.values())
                
            



        
        