class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        temp=money
        for i in range(2):
            money-=prices[i]
        if money < 0:
            return temp
        return money