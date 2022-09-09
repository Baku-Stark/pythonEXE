"""
should equal 9
should equal 16
should equal 32
should equal 45
should equal 64
"""

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    return number * 9