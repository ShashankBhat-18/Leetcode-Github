class Solution(object):
    def twoSum(self, nums, target):
        nums_dict={}
        result=[]
        for index,num in enumerate(nums):
            complement=target-num
            if complement in nums_dict:
                result.append(nums_dict[complement])
                result.append(index)
            nums_dict[num]=index
        return result
s=Solution()
nums=[2,7,11,15]
target=9
r=s.twoSum(nums,target)
print("Result: ",r)