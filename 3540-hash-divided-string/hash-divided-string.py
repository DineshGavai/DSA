import string
class Solution:
    def stringHash(self, s: str, k: int) -> str:
        string_list=list(string.ascii_lowercase)
        ascii_value=[]
        for i in s:
            ascii_value.append(string_list.index(i))
        res=""
        for i in range(0,len(ascii_value),k):
            idx=sum(ascii_value[i:i+k])
            res+=string_list[idx%26]
        return res

        




            