class Solution:
    def maximumTime(self, time: str) -> str:
        time_digits = list(time)
        question_mark = '?'

        if time_digits[0] == question_mark:
            if time_digits[1] != question_mark and int(time_digits[1]) > 3:
                h1 = 1
            else:
                h1 = 2
        else:
            h1 = int(time_digits[0])
            
        if time_digits[1] == question_mark:
            if h1 == 2:
                h2 = 3
            else:
                h2 = 9
        else:
            h2 = int(time_digits[1])

        if time_digits[3] == question_mark:
            m1 = 5
        else:
            m1 = int(time_digits[3])

        if time_digits[4] == question_mark:
            m2 = 9
        else:
            m2 = int(time_digits[4])


        return f"{h1}{h2}:{m1}{m2}"
