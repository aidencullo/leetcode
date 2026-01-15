class Solution:
    def dayOfYear(self, date: str) -> int:
        def leap_year(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            if year % 4 == 0:
                return True
            return False
        
        year, month, day = date.split('-')
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap_year(int(year)):
            days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefix = [0] + list(accumulate(days_in_month))
        month_idx = int(month) - 1
        return prefix[month_idx] + int(day)
