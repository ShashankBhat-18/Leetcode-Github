from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        write_index=0
        read_index=0
        while read_index<len(chars):
            count=1
            while read_index+1<len(chars) and chars[read_index]==chars[read_index+1]:
                read_index+=1
                count+=1
            chars[write_index]=chars[read_index]
            write_index+=1
            if count>1:
                for digit in str(count):     
                    chars[write_index]=digit
                    write_index+=1
            read_index+=1
        return write_index
