from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n=len(nums)
            right_prod=[1]*n
            left_prod=[1]*n
            left=1
            right=1
            for i in range (1,n):
                left*=nums[i-1]
                left_prod[i]=left
            for i in range(n-2,-1,-1):
                right*=nums[i+1]
                right_prod[i]=right
            result=[left_prod[i]*right_prod[i]for i in range(n)]
            return result
nums=[1,2,3,4]
s=Solution()
res=s.productExceptSelf(nums)
print(res)