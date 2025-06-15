class Solution:
    def maxDiff(self, num: int) -> int:
        nums=list(str(num))
        to_max=''
        to_min=''
        if len(nums)==1:
            to_max=nums[0]
            to_min=nums[0]
        
        for i in nums:
            if i != '9' and to_max == '':
                to_max=i
            if i != '1' and i != '0' and to_min == '':
                to_min=i
        max_val=''
        min_val=''
        to_change='1'
        if to_min != nums[0]:
            to_change='0'

        for i in nums:
            if i == to_max:
                max_val+='9'
            else:
                max_val+=i
            if i == to_min:
                min_val+=to_change
            else:
                min_val+=i
        return int(max_val) - int(min_val)