# 배열을 입력받아 output[i]가 자신을 제외한 나머지 요소의 곱셈 결과가 되도록 출력하라.
# 나눗셈을 하지 않고 O(n)에 풀이하라.

# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈

from ast import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    out = []
    p = 1

    for i in range(len(nums)):
        out.append(p)
        p = p*nums[i]
    
    for i in range(len(nums)-1, -1, -1):
        out[i] = out[i] * p
        p = p * nums[i]

    return out
