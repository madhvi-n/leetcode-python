from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = "%Y-%m-%d"

        # get the date objects for the two dates
        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)

        # calculate the difference between the two dates
        delta = date2_obj - date1_obj

        # extract the number of days from the difference
        num_days = delta.days
        return abs(num_days)