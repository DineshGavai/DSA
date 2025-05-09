class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res=0
        last_one=bank[0].count("1")
        for i in range(1,len(bank)):
            count_one=bank[i].count("1")
            if last_one==0 and count_one!=0:
                last_one=count_one
                pass
            elif count_one!=0:
                res+=last_one*count_one
                last_one=count_one
            else:
                pass
        return res


            