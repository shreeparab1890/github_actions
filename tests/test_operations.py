from src.operations import add, sub

def test_add():
    assert add(1,3) == 4
    assert add(5,5) == 10
    assert add(4,5) == 9
    assert add(1,-1) == 0

    
def test_sub():
    assert sum(1,-1) == 2
    assert sum(6,2) == 4
    assert sum(3,3) == 0
    assert sum(3,4) == -1
