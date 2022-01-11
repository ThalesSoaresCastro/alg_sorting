from ..ordena_alg.heapsort import heapsort

def test_heapsort():
    a = [4,3,2,1,8,7,6,5,5,5,5,7,1,24,8,9,543]
    b = a.copy()
    a.sort()
    heapsort(b)
    assert b == a

def test_array_unique_heapsort():
    a=[1]
    b = a.copy()
    heapsort(b)
    assert b == a

def test_array_empty_heapsort():
    a=[]
    b = a.copy()
    heapsort(b)
    assert b == a
