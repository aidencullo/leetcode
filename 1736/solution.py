from conditions import (
    is_h1_question_mark_and_h2_question_mark,
    is_h1_question_mark_and_h2_not_question_mark_and_h2_le_3,
    is_h1_question_mark_and_h2_not_question_mark_and_h2_gt_3,
    is_h2_question_mark_and_h1_computed_eq_2,
    is_h2_question_mark_and_h1_computed_ne_2,
    is_m1_question_mark,
    is_m2_question_mark,
)

class Solution:
    def maximumTime(self, t: str) -> str:
        h1_orig, h2_orig, _, m1_orig, m2_orig = t
        
        h1_computed = h1_orig
        if is_h1_question_mark_and_h2_question_mark(h1_orig, h2_orig):
            h1_computed = '2'
        if is_h1_question_mark_and_h2_not_question_mark_and_h2_le_3(h1_orig, h2_orig):
            h1_computed = '2'
        if is_h1_question_mark_and_h2_not_question_mark_and_h2_gt_3(h1_orig, h2_orig):
            h1_computed = '1'
        
        h2_computed = h2_orig
        if is_h2_question_mark_and_h1_computed_eq_2(h2_orig, h1_computed):
            h2_computed = '3'
        if is_h2_question_mark_and_h1_computed_ne_2(h2_orig, h1_computed):
            h2_computed = '9'
        
        m1_computed = m1_orig
        if is_m1_question_mark(m1_orig):
            m1_computed = '5'
        
        m2_computed = m2_orig
        if is_m2_question_mark(m2_orig):
            m2_computed = '9'
        
        return f"{h1_computed}{h2_computed}:{m1_computed}{m2_computed}"
