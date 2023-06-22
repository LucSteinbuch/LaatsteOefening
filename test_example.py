from example import add
from example import subtract


def test_add_positive():
        assert add(1,1) > 0
        
        
def test_subtract():
        assert subtract(1,1) == 0        
