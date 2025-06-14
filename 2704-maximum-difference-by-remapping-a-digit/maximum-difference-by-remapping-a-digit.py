class Solution:
    def minMaxDifference(self, num: int) -> int:
        to_max=''
        temp=list(str(num))
        for i in range(len(temp)):
            if temp[i] != '9':
                to_max=temp[i]
                break
        max_value=''
        for i in range(len(temp)):
            if temp[i]==to_max:
                max_value+='9'
            else:
                max_value+=temp[i]
    
        to_min=''
        min_value=''
        for i in range(len(temp)):
            if temp[i] != '0':
                to_min=temp[i]
                break
        for i in range(len(temp)):
            if temp[i]==to_min:
                min_value+='0'
            else:
                min_value+=temp[i]



        return int(max_value)-int(min_value)
