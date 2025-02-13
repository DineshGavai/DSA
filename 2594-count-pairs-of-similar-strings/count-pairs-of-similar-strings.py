class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res=0
        for i in range(len(words)):
            set_temp=set(words[i])
            freq_i=Counter(set_temp)
            for j in range(i+1,len(words)):
                set_temp2=set(words[j])
                freq_j=Counter(set_temp2)
                if freq_i==freq_j:
                    res+=1
        return res