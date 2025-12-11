def is_h1_question_mark_and_h2_question_mark(h1_orig, h2_orig):
    return h1_orig == '?' and h2_orig == '?'

def is_h1_question_mark_and_h2_not_question_mark_and_h2_le_3(h1_orig, h2_orig):
    return h1_orig == '?' and h2_orig != '?' and h2_orig <= '3'

def is_h1_question_mark_and_h2_not_question_mark_and_h2_gt_3(h1_orig, h2_orig):
    return h1_orig == '?' and h2_orig != '?' and h2_orig > '3'

def is_h2_question_mark_and_h1_computed_eq_2(h2_orig, h1_computed):
    return h2_orig == '?' and h1_computed == '2'

def is_h2_question_mark_and_h1_computed_ne_2(h2_orig, h1_computed):
    return h2_orig == '?' and h1_computed != '2'

def is_m1_question_mark(m1_orig):
    return m1_orig == '?'

def is_m2_question_mark(m2_orig):
    return m2_orig == '?'

