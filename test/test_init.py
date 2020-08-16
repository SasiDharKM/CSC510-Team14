import code as cd

def test_answer_fail():
    assert cd.inc(3) == 5
    
def test_answer_pass():
    assert cd.inc(4) == 5
