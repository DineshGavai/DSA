class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date=date.split('-')
        year=str(format(int(date[0]),'016b'))
        month=str(format(int(date[1]),'04b'))
        day=str(format(int(date[2]),'05b'))
        combined=f"{year.lstrip('0')}-{month.lstrip('0')}-{day.lstrip('0')}"
        return combined