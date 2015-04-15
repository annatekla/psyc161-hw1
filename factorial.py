#!usr/bin/env python
"""Module for estimation of factorial (Homework #1)

Note:  this is just a skeleton for you to work with.  But it already
       has some "bugs" you need to catch and fix.
"""

from nose.tools import assert_equal


def factorial_recursive(n):
    """Asserts that the n entered for number of conditions is an integer.
    If n < 1 it returns 1 and otherwise it uses a recursive function to
    estimate the number of possible trial orders."""
    if int(n) < 0:
        print 'WARNING: Number of conditions must not be negative'
    elif 0 <= int(n) <= 1:
        pass  # does nothing
        return 1
    else:
        return int(n) * (factorial_recursive(int(n) - 1))


def test_factorial():
    """Test factorial function"""
    assert_equal(factorial_recursive(1), 1)
    assert_equal(factorial_recursive(0), 1)
    assert_equal(factorial_recursive(12), 479001600)
    assert_equal(factorial_recursive(5), 120)
    assert_equal(factorial_recursive(-24), None)


if __name__ == '__main__':
    # This is a way to determine either file was "executed", so if it was
    # imported (by e.g. nose) as a library, we should not run code
    # below

    print test_factorial.__doc__
    nconditions = raw_input("Please enter number of conditions: ")
    norders = factorial_recursive(nconditions)
    print ("Number of possible trial orders: " + str(norders))
