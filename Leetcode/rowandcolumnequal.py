from typing import List
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i]==[row[j] for row in grid]:
                    count+=1
        return count