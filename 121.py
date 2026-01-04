class Solution:
    def maxProfit(prices):
        minp=float('inf') # khoi tao gia mua thap nhat la vo cung
        maxp=0

        for p in prices:
            if p < minp:
                minp=p # cap nhat gia mua thap nhat neu co gia thap hon
            elif p-minp>maxp:
                maxp=p-minp # tinh loi nhuan neu ban gia hien tai
        return maxp
        