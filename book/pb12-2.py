# 주식을 사고팔기 가장 좋은 시점
# 한번의 거래로 낼 수 있는 최대 이익을 산출하라.

# 저점과 현재 값과의 차이 계산

from ast import List
import sys


def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price-min_price)
    return profit