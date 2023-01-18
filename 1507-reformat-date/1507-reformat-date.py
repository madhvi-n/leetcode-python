class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        
        months = {
            "Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
            "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"
        }
        
        currMonth = months.get(month)
        day = day[:len(day) - 2]
        
        if int(day) < 10:
            day = '0' + day
            
        return "{}-{}-{}".format(year, currMonth, day)