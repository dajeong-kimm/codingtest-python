# 주식을 사고팔기 가장 좋은 시점
# 한번의 거래로 낼 수 있는 최대 이익을 산출하라.

# 브루트 포스로 계산

from ast import List


def maxProfit(self, prices: List[int]) -> int:
    max_price = 0

    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j]-price, max_price)
    return max_price
        