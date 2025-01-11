class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return[-1,-1]
        res=[]
        try:
            starting_index=nums.index(target)
        except:
            starting_index=-1
        end_index=-1
        if starting_index != -1:
            temp=starting_index
            for i in range(starting_index,len(nums)-1):
                if nums[i+1]==nums[i]:
                    temp+=1
                else:
                    end_index=temp
                    break
            end_index=temp
                
                
        if starting_index != -1 and end_index ==-1:
            end_index=0
        res.append(starting_index)
        res.append(end_index)
        return res

            