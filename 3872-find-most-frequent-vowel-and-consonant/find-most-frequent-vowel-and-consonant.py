class Solution:
    def maxFreqSum(self, s: str) -> int:
        consonants={}
        vowels={}
        v=set("aeiou")
        for i in s:
            if i in v:
                if i in vowels:
                    vowels[i]+=1
                else:
                    vowels[i]=1
            else:
                if i in consonants:
                    consonants[i]+=1
                else:
                    consonants[i]=1
        a,b=0,0
        if vowels:
            a=max(vowels.values())
        if consonants:
            b=max(consonants.values())

        return a+b        
        
            
