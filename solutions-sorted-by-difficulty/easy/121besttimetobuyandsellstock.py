class Solution(object):
    def maxProfit(self, prices):
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            else:
                maxProfit = max(maxProfit, price - minPrice)

        return maxProfit

solution = Solution()
print(solution.maxProfit([2, 4, 1,5]))




solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4] ))
