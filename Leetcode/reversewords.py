class Solution:
    def reverseWords(self, s: str) -> str:
        list=s.split()
        result=""
        for i in list[::-1]:
            result=result+i+" "
        return result.strip()
s=Solution()
r=s.reverseWords("Hello this is shashank")
print(r)