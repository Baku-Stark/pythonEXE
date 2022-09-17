'''
test.assert_equals(sum_no_duplicates([1, 1, 2, 3]), 5)
test.assert_equals(sum_no_duplicates([1, 1, 2, 2, 3]), 3)
'''

def sum_no_duplicates(l):
    return sum(n for n in set(l) if l.count(n) == 1)