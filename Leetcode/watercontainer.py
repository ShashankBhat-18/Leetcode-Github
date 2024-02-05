from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        #index1,index2=0,0
        lef_most=0
        right_most=len(height)-1
        while lef_most<right_most: 

            h=min(height[lef_most],height[right_most])
            w=right_most-lef_most
            current_area=h*w

            max_area=max(max_area,current_area)

            if(height[lef_most]<height[right_most]):
                lef_most+=1
            else:
                right_most-=1
            
        return max_area