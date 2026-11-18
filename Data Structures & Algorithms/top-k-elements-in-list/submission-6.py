# most frequent elements within the array
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for num in nums:
            # ctr[num] = ctr.get(ctr[num], 0) + 1 
            # ctr[num] 이 없는 상태에서 꺼내려고 하면 Keyerror 발생
            ctr[num] = ctr.get(num, 0) + 1 # num이라는 key의 값을 주고, 없다면 0

        s_ctr = sorted(ctr, key=lambda x: ctr[x])
        # sorted(dict) -> Key를 기준으로 정렬해버림.
        # 그래서 key= 인자를 통하여 sorted의 정렬 key를 정해주는데, 여기에 lambda로 ctr[x]
        # "키들을 정렬하되, 비교할 때는 각 키의 빈도를 보라"

        result = s_ctr[-1:-1-k:-1]
        # reverse 활용 및 더 축약하면 이렇게도 가능.
        # s_ctr = sorted(ctr, key=lambda x: ctr[x], reverse=True)
        # return s_ctr[:k]

        return result


