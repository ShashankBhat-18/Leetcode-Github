from collections import Counter
from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count=Counter(arr)
        print(count)
        return len(set(count.values()))==len(count)
    
s=Solution()
arr = [1, 2, 2, 1, 1, 3]
result = s.uniqueOccurrences(arr)
print(result)
