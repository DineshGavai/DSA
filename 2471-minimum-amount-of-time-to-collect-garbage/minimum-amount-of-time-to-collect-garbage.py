class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        plastic=0
        glass=0
        metal=0
        travel.append(0)
        n=len(garbage)
        last_p=0
        last_g=0
        last_m=0

        for i in range(n):
            if "P" in garbage[i]:
                p_count=garbage[i].count("P")
                plastic+=p_count
                last_p=i
            if "G" in garbage[i]:
                p_count=garbage[i].count("G")
                glass+=p_count
                last_g=i
            if "M" in garbage[i]:
                p_count=garbage[i].count("M")
                metal+=p_count
                last_m=i
            
        travel_sum=sum(travel[0:last_p])
        travel_sum+=sum(travel[0:last_g])
        travel_sum+=sum(travel[0:last_m])
        res=travel_sum+plastic+metal+glass
        return res
            

        