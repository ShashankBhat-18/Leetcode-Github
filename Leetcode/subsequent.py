class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lst=list(s)
        new=[]
        count=0
        for i in t:
            if i in lst:
                count+=1
                new.append(i)
        if new==lst:
            return True
        else:
            return False
s=Solution()
str = "axc"
t = "ahbgdc"
print(s.isSubsequence(str,t))
