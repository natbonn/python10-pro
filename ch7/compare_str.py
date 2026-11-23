"""String comparison examples"""
from ch7.interning_and_compare import are_equal

s1 = "Andrew"
s2 = "andrew"

are_equal(s1, s2)  # import

# 'A' < "a" (ASCII 65 < 97)
is_s1_lt_s2 = s1 < s2     # True
is_s1_gt_s2 = s1 > s2     # False
