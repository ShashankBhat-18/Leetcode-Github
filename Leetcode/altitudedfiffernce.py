from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_value=float("-inf")
        new_list=[0]
        diff=0
        for i in gain:
            diff+=i
            new_list.append(diff)
        for j in new_list:
            max_value=max(max_value,j)
        return max_value
    
s=Solution()
gain = [-5, 1, 5, 0, -7]
print(s.largestAltitude(gain))


