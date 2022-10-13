'''
import codewars_test as test
from solution import powers_of_two

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(powers_of_two(0), [1])
        test.assert_equals(powers_of_two(1), [1, 2])
        test.assert_equals(powers_of_two(4), [1, 2, 4, 8, 16])
'''

def powers_of_two(n):
    return [2**i for i in range(n+1)]
