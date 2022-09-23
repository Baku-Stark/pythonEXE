'''
@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(feast("great blue heron", "garlic naan"), True)
        test.assert_equals(feast("chickadee", "chocolate cake"), True)
        test.assert_equals(feast("brown bear", "bear claw"), False)
'''

def (beast, dish):
	return True if beast[0] == dish[0] and beast[-1] == dish[-1] else False