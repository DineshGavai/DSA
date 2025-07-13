class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res=0
        i=0
        j=0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
              i+=1
              j+=1
              res+=1
            elif  players[i] > trainers[j]:
                j+=1
            
        return res

            
           