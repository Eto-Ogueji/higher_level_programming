def this_raises():
    r"""This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
        File "c:\Users\Eto Ogueji\Desktop\higher_level_programming\0x07-test_driven_development\raise_runtime_error.py", line 1, in <module>
            raise RuntimeError('here is the error')
    RuntimeError: here is the error
    """
    raise RuntimeError('here is the error')

import doctest
doctest.testmod()