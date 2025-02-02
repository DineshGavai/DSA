class Solution:
    def check(self, nums: List[int]) -> bool:
        def rotate(arr,k):
            # arr=nums.copy()
            n=len(arr)
            k=k%n
            temp=arr[-k:]
            arr[k:]=arr[:-k]
            arr[:k]=temp
            return arr
        sorted_arr=sorted(nums)
        if sorted_arr==nums:
            return True
        for i in range(1,len(nums)+1):
            rotate_arr=rotate(nums,1)
            print(rotate_arr)
            if rotate_arr==sorted_arr:
                return True
        return False