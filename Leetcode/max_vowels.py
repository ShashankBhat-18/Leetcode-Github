from typing import List
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vow=['a','e','i','o','u']
        window_slit = s[:k]
        current_count=sum(1 for char in window_slit if char in vow)
        max_count=current_count
        for i in range(k,len(s)):
            if s[i-k] in vow:
                current_count-=1
            if s[i] in vow:
                current_count+=1
            max_count=max(max_count,current_count)
        return max_count
    

s = "abciiidef"
k = 3
solution = Solution()
result = solution.maxVowels(s, k)
print(result)
