import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        pq=[]
        for element in freq:
            heapq.heappush(pq, (-freq[element],element))
        listOfitems=[]
        while k:
            _,item=heapq.heappop(pq)
            listOfitems.append(item)
            k-=1
        return listOfitems

solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,2,2,3],2))