class Solution:
    def minMaxDifference(self, num: int) -> int:
        to_max=''
        to_min=''
        temp=list(str(num))
        for i in range(len(temp)):
            if temp[i] != '9' and to_max=='':
                to_max=temp[i]
            if temp[i] != '0'and to_min=='':
                to_min=temp[i]
                
        max_value=''
        min_value=''
        for i in range(len(temp)):
            if temp[i]==to_max:
                max_value+='9'
            else:
                max_value+=temp[i]
            if temp[i]==to_min:
                min_value+='0'
            else:
                min_value+=temp[i]
            



        return int(max_value)-int(min_value)
