class Solution:
    def isPalindrome(self, s: str) -> bool:
        seen = {}

        # [기존 코드]
        # ss = s.replace(" ", "")
        # sss = "".join(char for char in ss if ss.isalpha())
        # prep = list(sss.lower())
        #
        # 문제점
        # 1. ss.isalpha() -> 글자 하나(char)가 아니라 문자열 전체(ss)를 검사함
        #    -> char.isalpha() 처럼 반복 변수로 검사해야 함
        # 2. isalpha()는 숫자까지 지움 -> 문제는 영문자 + 숫자를 남기라고 함 -> isalnum()
        # 3. replace(" ", "")는 불필요 -> 공백은 isalnum()에서 False라 자동으로 걸러짐
        # 4. list()는 불필요 -> 문자열도 인덱싱/슬라이스 가능

        # [개선 코드] 필터링 + 소문자 변환을 한 줄로
        prep = "".join(c.lower() for c in s if c.isalnum())

        return prep == prep[::-1]

    

        # for p in range(len(prep)):
        #     if prep[p] not in seen:
        #         seen[prep[p]] = seen.get(prep[p],0) + 1
        #     else:
        #         seen[prep[p]] = seen.get(prep[p]) - 1
        # print(seen)
        # if sum(seen.values()) == 0:
        #     return True
        # else:
        #     return False





