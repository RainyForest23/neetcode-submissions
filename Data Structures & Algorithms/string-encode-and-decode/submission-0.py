class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s   # "길이#내용"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0                               # 지금 읽는 위치
        while i < len(s):
            j = i
            while s[j] != "#":              # '#'까지 이동하며 길이 숫자 찾기
                j += 1
            length = int(s[i:j])            # '#' 앞부분이 길이
            start = j + 1                   # 내용은 '#' 바로 다음부터
            res.append(s[start:start + length])
            i = start + length              # 다음 문자열의 시작 위치로 점프
        return res