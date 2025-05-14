class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:    
        user_minutes = defaultdict(set)
        
        for user_id, minute in logs:
            user_minutes[user_id].add(minute)   
        
        res=[0] * k
        for key,value in user_minutes.items():
            to_update=len(value)
            if to_update > 0:
                res[to_update-1]+=1
        return res
