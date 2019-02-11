nose-ittr
=========
This is a Python 3 port of the nose-ittr extension created by Sergey Ragatsky.

nose extension for supporting parametrized testing.
---------------------------------------------------
Allows developer to run the same test over and over again using different values

Main Features:
 * Very easy to integrate with existing tests
 * Saves a lot of boilerplate code, and code replication
 * Work with all nose plugins (including multiprocessing)
 * Customize setup per test, by using this package built-in nose plugin setup-ittr

Installation:
-------------

.. code-block:: shell

    pip3 install nose_ittr

Basic usage:
------------

.. code-block:: python

    import math

    from nose.tools import assert_equal, assert_not_equal
    from nose_ittr import IttrMultiplier, ittr

    class TestFoo(object, metaclass=IttrMultiplier):
        
        @ittr(number=[1, 2, 3, 4])
        def test_even(self):
            assert_equal(self.number % 2, 0)            
        
        @ittr(numerator=[15, 6], denominator=[2, 3])
        def test_no_remainder(self):
            assert_equal(self.numerator % self.denominator, 0)

        @ittr(value=[4, 14])
        def test_prime_with_custom_setup(self):
            for i in range(3, int(math.sqrt(self.value))):
                assert_not_equal(self.value % i, 0)

.. code-block:: shell

    nosetests --with-setup-ittr [for setup customization support]

result:
                   
.. code-block:: shell

        TestFoo.test_even_1 ... FAIL
        TestFoo.test_even_2 ... .ok
        TestFoo.test_even_3 ... FAIL
        TestFoo.test_even_4 ... .ok
        TestFoo.test_no_remainder_2_6 ... .ok
        TestFoo.test_no_remainder_2_15 ... FAIL
        TestFoo.test_no_remainder_3_6 ... .ok
        TestFoo.test_no_remainder_3_15 ... .ok
        TestFoo.test_prime_with_custom_setup_14 ... ok
        TestFoo.test_prime_with_custom_setup_4 ... ok


**Notes:**
 * Doesn't affect test docstring if used with -v parameter.

To change the docstring printout based on the varibales passed to test, use the plugin 
`nose-docstring-modifier <https://pypi.python.org/pypi/nose-docstring-modifier/>`_.

:Authors:
    Sergey Ragatsky 
:Contributors: 
    Niv Mizrahi

    Tal Ben Basat

    Nicole Franco  

    Roy Klinger 
 
    Maroun Maroun

    Siobhan Dolan

    Kate Kligman
