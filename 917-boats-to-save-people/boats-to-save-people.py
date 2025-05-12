class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        res = 0
        people.sort()
        i, j = 0, len(people) - 1
        while i <= j:
            if i == j:
                res += 1
                break

            if people[i] + people[j] <= limit:
                res += 1
                i += 1
                j -= 1
            else:
                res+=1
                j -= 1

        return res
