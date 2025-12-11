class Solution:
    def maximumTime(self, time: str) -> str:
        initial_h1 = time[0]
        initial_h2 = time[1]
        initial_m1 = time[3]
        initial_m2 = time[4]
        question_mark = '?'

        if initial_h1 == question_mark:
            if initial_h2 != question_mark and int(initial_h2) > 3:
                h1 = 1
            else:
                h1 = 2
        else:
            h1 = int(initial_h1)
            
        if initial_h2 == question_mark:
            if h1 == 2:
                h2 = 3
            else:
                h2 = 9
        else:
            h2 = int(initial_h2)

        m1 = 5 if initial_m1 == '?' else initial_m1
        m2 = 9 if initial_m2 == '?' else initial_m2

        return f"{h1}{h2}:{m1}{m2}"
