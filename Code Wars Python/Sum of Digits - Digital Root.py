def digital_root(n):
    


# ------
import codewars_test as test
from solution import digital_root

@test.describe("Sum of Digits / Digital Root")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(digital_root(16), 7)
        # 16  -->  1 + 6 = 7  
        test.assert_equals(digital_root(942), 6)
        # 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
        test.assert_equals(digital_root(132189), 6)
        # 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
        test.assert_equals(digital_root(493193), 2)
        # 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2