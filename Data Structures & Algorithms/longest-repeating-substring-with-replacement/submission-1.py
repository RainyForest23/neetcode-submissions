# find maximum lenght of substring

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}   # 창문 안 글자별 개수
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1   # 1. 오른쪽 글자를 창문에 넣기

            # 2. 바꿔야 할 개수가 k를 넘으면 유효하지 않음 → 왼쪽에서 하나씩 빼기
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)   # 3. 유효한 창문 길이로 최댓값 갱신

        return res