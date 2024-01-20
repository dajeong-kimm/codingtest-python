#투 포인터를 이용한 스왑

from ast import List


def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) -1
    while left < right:
        s[left] , s[right] = s[right], s[left]
        left += 1
        right -= 1