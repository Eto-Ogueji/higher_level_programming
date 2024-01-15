# doctest_ellipses.py

class MyClass:
    pass

def unpredictable(obj):
    """Returns a new list containing obj.
    
    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<__main__.MyClass object at 0x...>]
    """
    return [obj]

import doctest
doctest.testmod()