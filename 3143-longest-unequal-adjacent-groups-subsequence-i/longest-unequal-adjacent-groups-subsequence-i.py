class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res=[words[0]]
        val=groups[0]
        for i in range(1,len(words)):
            if val==groups[i]:
                continue
            res.append(words[i])
            val=groups[i]
        return res

