from ..ordena_alg.quicksort import quicksort

def test_quicksort():
    a = [4,3,2,1,8,7,6,5,5,5,5,7,1,24,8,9,543]
    b = a.copy()
    a.sort()
    quicksort(b,0, len(b)-1)
    assert b == a

def test_array_unique_quicksort():
    a=[1]
    b = a.copy()
    quicksort(b,0, len(b)-1)
    assert b == a

def test_array_empty_quicksort():
    a=[]
    b = a.copy()
    quicksort(b,0, len(b)-1)
    assert b == a