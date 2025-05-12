class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        from collections import Counter
        
        count = Counter(digits)
        res = set()

        for i in range(1, 10):  # hundreds place, can't be 0
            if count[i] == 0:
                continue
            count[i] -= 1

            for j in range(0, 10):  # tens place
                if count[j] == 0:
                    continue
                count[j] -= 1

                for k in range(0, 10, 2):  # units place (must be even)
                    if count[k] == 0:
                        continue
                    res.add(i * 100 + j * 10 + k)

                count[j] += 1  # restore j

            count[i] += 1  # restore i

        return sorted(res)
