# anagram : have to use whole character of original string regardless of its order
# compare length first
# compare key and value of dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s.len() != t.len(): 
        # len() 은 매서드가 아니라 내장 함수임.
        if len(s) != len(t):
            return False
        else:
            s_dict = {}
            t_dict = {}
            for i in s:
                if s_dict.get(i, 0) == 0:
                    s_dict[i] = 1
                    
                else:
                    s_dict[i] = s_dict[i]+1
            # print(s_dict)
                
            for j in t:
                if t_dict.get(j, 0) == 0:
                    t_dict[j] = 1
                else:
                    t_dict[j] = t_dict[j]+1
            # print(t_dict)
        
        if s_dict == t_dict:
            return True
        else:
            return False

        