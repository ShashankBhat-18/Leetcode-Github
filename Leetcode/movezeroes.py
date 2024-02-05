from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        new=[]
        i=0
        while i<len(nums):
            if nums[i]==0:
                new.append(nums[i])
                nums.pop(i)
            else:
                i+=1
        nums.extend(new)
        print(nums)
        
s=Solution()
nums=[0,1,0,3,12]
s.moveZeroes(nums)
