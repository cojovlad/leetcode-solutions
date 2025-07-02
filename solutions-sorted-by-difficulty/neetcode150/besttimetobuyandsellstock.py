class Solution(object):
    def maxProfit(self, prices):
        smallestToTheLeftOfValue={}
        smallestValue=prices[0]
        for i,price in enumerate(prices):
            smallestToTheLeftOfValue[i]=smallestValue
            if price<smallestValue:
                smallestValue=price
        maxValue=0
        for element in smallestToTheLeftOfValue:
            sum=prices[element]-smallestToTheLeftOfValue[element]
            if(sum>maxValue):
                maxValue=sum
        return maxValue
solution = Solution()
print(solution.maxProfit([10,1,5,6,7,1]))