from itertools import count


class Solution(object):
    #Chapter 4
    def quickSort(self,nums):
        if len(nums)<=1:
            return nums
        else:
            pivot =nums[0]
            less = [i for i in nums[1:] if i<= pivot]

            greater = [i for i in nums[1:] if i > pivot]

            return self.quickSort(less) + [pivot] + self.quickSort(greater)

    def maximumNumber(self, max, nums):
        if (len(nums) == 0):
            return 0
        if len(nums) == 1:
            if nums[0] > max:
                return nums[0]
        else:
            if nums[0] > max:
                max = nums[0]
            return self.maximumNumber(max, nums[1:])
        return max

    #Chapter 2
    def findSmallest(self, nums):
        smallest = nums[0]
        smallestIndex = 0
        for i in range(len(nums)):
            if nums[i] < smallest:
                smallest = nums[i]
                smallestIndex = i
        return smallestIndex
    def selectionSort(self, nums):
        newArr=[]
        for i in range(len(nums)):
            smallest = self.findSmallest(nums)
            newArr.append(nums.pop(smallest))
        return newArr

    #Chapter 1
    def binarySearch(self, nums,x):
        low=0
        high=len(nums)-1
        nums=self.quickSort(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==x:
                return mid
            if x<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1

solution = Solution()
print(solution.binarySearch([1,2,3,4,3,6,7,8,10,9],8))
#1.1 7 steps
#1.2 8 steps
#1.3 o log n
#1.4 o n
#1.4 o n
#1.4 o n

#2.1 l lists
#2.2 l lists
#2.3 array
#2,4 you have to make space for him
#2.5 faster

#3.1 we have two functions called, the name is maggie, greet2 didn t go off yet and greet2 is being called inside greet
#3.2 stack overflow
#4.1
def sumOfNumbers(self,nums):
    if(len(nums)==0):
        return 0
    if len(nums)==1:
        return nums[0]
    else:
        return nums[0]+sumOfNumbers(nums[1:])
#4.2
def countOfNumbers(self,nums):
    if(len(nums)==0):
        return 0
    if len(nums)==1:
        return 1
    else:
        return 1+countOfNumbers(nums[1:])
#4.3
def maximumNumber(self,max,nums):
    if(len(nums)==0):
        return 0
    if len(nums)==1:
        if nums[0]>max:
            return nums[0]
    else:
        if nums[0]>max:
            max=nums[0]
            return maximumNumber(max,nums[1:])
#4.4 base case low>high and we recall binarySearch with mid+1 for x>nums[mid] and mid-1 otherwise for the high
#4.5 o n
#4.6 o n
#4.7 o 1
#4.8 o n^2

#5.1 consistent
#5.2 inconsistent but because we know it returns always a rand it can be consistent
#5.3 inconsistent
#5.4 consistent
#5.5 C
#5.6 B
#5.7 B


