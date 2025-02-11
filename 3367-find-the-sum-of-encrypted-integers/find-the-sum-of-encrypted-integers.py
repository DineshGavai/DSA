class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encript(n):
            arr=[]
            while n > 0 :
                arr.append(n%10)
                n//=10
            max_elem=max(arr)
            
            for i in range(len(arr)):
                arr[i]=str(max_elem)
            return int("".join(arr))
        res=0
        for i in nums:
            res+=encript(i)
        return res
