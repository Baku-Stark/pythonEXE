"""
test.assert_equals(array_plus_array([1, 2, 3], [4, 5, 6]), 21)
test.assert_equals(array_plus_array([-1, -2, -3], [-4, -5, -6]), -21)
test.assert_equals(array_plus_array([0, 0, 0], [4, 5, 6]), 15)
test.assert_equals(array_plus_array([100, 200, 300], [400, 500, 600]), 2100)
"""


def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)