# use sliding window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        left = 0

        no_dup = set()

        for right in range(len(s)):
            while s[right] in no_dup:   # 새 글자가 window에 있는 동안
                no_dup.remove(s[left])  # 왼쪽 글자를 하나씩 없애고
                left += 1               # 왼쪽 인덱스를 늘려서
            no_dup.add(s[right])        # 오른쪽 글자를 집어넣기 (오른쪽 끝 늘리기)
            length = max(length, right-left+1)
        return length
        #     if s[right] not in no_dup: # is not in 아님!!!!!!!! Not in !!!
        #         no_dup.add(s[right]) # set은 .add, list는 .append
        #         length = right - left
        #     else:
        #         for item in range(left,right):
        #             no_dup.remove(no_dup[item])
        #     no_dup.add(s[right])
        #     left = right
        # length = lenght + 1
        # return length

