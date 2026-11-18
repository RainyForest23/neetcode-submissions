# most frequent elements within the array
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for num in nums:
            # ctr[num] = ctr.get(ctr[num], 0) + 1 
            # ctr[num] 이 없는 상태에서 꺼내려고 하면 Keyerror 발생
            ctr[num] = ctr.get(num, 0) + 1 # num이라는 key의 값을 주고, 없다면 0

        s_ctr = sorted(ctr, key=lambda x: ctr[x])
        result = s_ctr[-1:-1-k:-1]

        return result


