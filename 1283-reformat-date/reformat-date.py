class Solution:
    def reformatDate(self, date: str) -> str:
        month=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        temp=date.split(" ")
        year=temp[-1]
        month=month.index(temp[1])+1
        if month < 10:
            month=f"0{month}"
        day=""
        for i in range(len(temp[0])):
            if temp[0][i].isdigit():
                day+=temp[0][i]
            else:
                break
        if int(day) < 10:
            day=f"0{day}"

        return f"{year}-{month}-{day}"