class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        visited=set()
        for i in s:
            if i not in visited:
                first_idx=s.find(i)
                sec_idx=s.find(i,first_idx+1)
                distance_found=sec_idx-first_idx-1
                dis_index=ord(i)-ord('a')
                if distance[dis_index]!=distance_found:
                    return False
                
                visited.add(i)
        return True