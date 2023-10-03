import math

def test_sqr():
    num = 25
    assert math.sqrt(num) == 5

     
def test_square():
    num = 7
    assert num*num == 49

def test_fun():
    num = 5
    assert num+1 == 6

def test_multiply():
    num1, num2 = 3, 2
    assert num1*num2 == 6 

def test_check():
    x = 120
    assert x >= 100