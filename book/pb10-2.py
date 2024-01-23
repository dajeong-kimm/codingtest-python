#n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

from ast import List


def arrayPairSum(self, nums:List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i%2==0:
            sum += n

    return sum
