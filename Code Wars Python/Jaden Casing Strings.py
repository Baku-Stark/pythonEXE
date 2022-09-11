def to_jaden_case(string):
    textArr = string.split(" ")
    jadenCaseArr = []

    for word in textArr:
    	jadenCaseArr.append(word.capitalize())

    return " ".join(jadenCaseArr)

# =============================================
# Método 2
def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())

# =============================================
# Método 3
import string
toJadenCase = string.capwords


# ------
from solution import to_jaden_case
import codewars_test as test


@test.describe('Sample test')
def basic_tests():
    @test.it('Simple text')
    def _():
        quote = "How can mirrors be real if our eyes aren't real"
        test.assert_equals(to_jaden_case(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")