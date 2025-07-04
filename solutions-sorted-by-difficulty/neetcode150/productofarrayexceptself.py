class Solution(object):
    def productExceptSelf(self, nums):
        prod=1
        prodWithoutZero=1
        zeroCount=0
        for num in nums:
            prod*=1*num
            if num!=0:
                prodWithoutZero*=1*num
            else:
                zeroCount+=1
        newNums=[]
        for num in nums:
            if(zeroCount>1):
                newNums.append(0)
            elif zeroCount==1:
                if num == 0:
                    newNums.append(prodWithoutZero)
                else:
                    if prod==0:
                        newNums.append(0)
            else:
                newNums.append(prod//num)
        return newNums

solution = Solution()
print(solution.productExceptSelf([-1,0,1,2,0]))