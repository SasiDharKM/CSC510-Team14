# content of __init__.py
def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 5
    
def test_answer_passing():
    assert inc(4) == 5