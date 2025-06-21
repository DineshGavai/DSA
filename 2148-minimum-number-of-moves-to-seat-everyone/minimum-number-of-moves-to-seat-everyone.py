class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n=len(seats)
        res=0
        for i in range(n):
            if seats[i]!=students[i]:
                res+=abs(seats[i]-students[i])
        return res