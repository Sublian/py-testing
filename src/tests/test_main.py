
import pytest
#archivo a testear
from src.main import sum, greater_than,login

def test_sum():
    assert sum(2,5) ==7
    
def test_greater_than():
    assert greater_than(10,2)

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (5,1,6),
        (20,10,30),
        (sum(25,25),1,51),
        (15,sum(4,2),21),
        (sum(-10,5),sum(1,6),2)
    ]
)
def test_sum_params(input_x, input_y, expected):
    assert sum(input_x, input_y) == expected
    
def test_login_pass():
    assert login("sublian","python")
    
def test_login_fail():
    assert not login("Sublian","Python")