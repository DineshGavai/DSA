class Solution:
    def generateTheString(self, n: int) -> str:
        a = "ab"
        if n % 2 == 0:
            return a[0] * (n - 1) + a[1]
        else:
            return a[0] * n
