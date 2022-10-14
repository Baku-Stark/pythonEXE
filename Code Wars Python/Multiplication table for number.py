'''
import codewars_test as test
from solution import multi_table

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(multi_table(5), '1 * 5 = 5\n2 * 5 = 10\n3 * 5 = 15\n4 * 5 = 20\n5 * 5 = 25\n6 * 5 = 30\n7 * 5 = 35\n8 * 5 = 40\n9 * 5 = 45\n10 * 5 = 50')
        test.assert_equals(multi_table(1), '1 * 1 = 1\n2 * 1 = 2\n3 * 1 = 3\n4 * 1 = 4\n5 * 1 = 5\n6 * 1 = 6\n7 * 1 = 7\n8 * 1 = 8\n9 * 1 = 9\n10 * 1 = 10')
'''

def multi_table(number):
    set = ""
    for i in range(1, 11):
        res = i*number
        if i == 10:
            set += f"{i} * {number} = {res}"
        else:
            set += f"{i} * {number} = {res}\n"
    return set
