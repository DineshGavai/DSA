class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        val=bin(start^goal)
        return val.count('1')