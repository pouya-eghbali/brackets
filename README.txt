Brackets
========

.. figure:: https://github.com/pooya-eghbali/brackets/raw/master/logo.png
   :alt: Python Brackets

Brackets is a yet-another, a not just a pre-processor, a language built
on top of Python, allowing to use {} instead of indentation in Python,
and it allows defining powerful anonymous functions and introduces much
more sugar and candy into Python's syntax and abilities.

Visit `Brackets Website <http://python-brackets.org>`__ for examples and
more info or `read the docs <http://docs.python-brackets.org>`__.
Project is hosted on
`github <http://github.com/pooya-eghbali/brackets>`__.

Some examples:

::

    // Use braces in Python!

    def fib(n) {
      a, b = 0, 1
      while (a < n) {
        print(a, end=' ')
        a, b = b, a+b
      }
      print()
    }

    /*
      Powerful anonymous functions
    */

    print([def(x) {
      if(x in [0, 1]) {
        return x
      };
      while (x < 100) {
        x = x ** 2
      };
      return x
    }(x) for x in range(0, 10)])

Visit `Brackets Website <http://python-brackets.org>`__ for examples and
more info or `read the docs <http://docs.python-brackets.org>`__ to know
how it should be used.
