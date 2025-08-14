import random
from src.calculator import *

def add_random():
    return random.randint(1,100), random.randint(1,100)

def test_add():
    a,b = add_random()
    result = calculate(a, b, "1") 
    print(f"Num 1:{a} + Num 2:{b} = {result}")
    assert result == a + b
def test_sub():
    a,b = add_random()
    result = calculate(a, b, "2")
    print(f"Num 1:{a} - Num 2:{b} = {result}")
    assert calculate(a, b, "2") == a - b
def test_mul():
    a,b = add_random()
    result = calculate(a, b, "3")
    print(f"Num 1:{a} * Num 2:{b} = {result}")
    assert result == a * b
def test_div():
    a,b = add_random()
    result = calculate(a, b, "4")
    print(f"Num 1:{a} / Num 2:{b} = {result}")
    assert result == a / b

# python -m pytest -s