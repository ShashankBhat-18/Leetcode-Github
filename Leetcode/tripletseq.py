from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        min_num=float("inf")
        sec_min=float("inf")

        for num in nums:
            if num<=min_num:
                min_num=num
            elif num<=sec_min:
                sec_min=num
            else:
                return True
        return False