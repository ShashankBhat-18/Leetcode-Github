from typing import List 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum=sum(nums[:k])
        max_avg=window_sum/k
        for i in range(k,len(nums)):
            window_sum=window_sum-nums[i-k]+nums[i]
            max_avg=max(max_avg,window_sum/k)
        return max_avg
        

s=Solution()
nums = [1, 12, -5, -6, 50, 3]
k = 4
result = s.findMaxAverage(nums, k)
print(result)


'''MY CODE , VERY SLOW 
        max_avg=0
        n=k
        i=0
        while n<len(nums):
            newmax=(sum(nums[i:n]))/k
            if newmax>max_avg:
                max_avg=newmax
            i+=1
            n+=1
        return max_avg'''
