Functions
=========

Functions, are a little different in Brackets. Brackets has several different
types of functions. To define a regular function like python functions, you
can do:

.. code-block:: java

    def function_name(args and kwargs) {
       ...do whatever
       return whatever
    }

We still have Python lambdas::

    lambda x: x**2

But, we have more powerful anonymous functions [they're not really anonymous
though]:

.. code-block:: java

    def (args, kwargs) {
       ...anything
       return something
    }

these can be used just like lambdas:

.. code-block:: c++

    # Fibonacci
    print([def(x){
        if(x in [0, 1]) {
          return x
        };
        while (x < 100) {
          x = x ** 2
        };
        return x
      }(x) for x in range(0, 10)])

and of-course, again, you can do all of it in one line:

.. code-block:: java

    print([def(x) { if(x in [0, 1]) {return x}; while (x < 100) { x = x ** 2} return x}(x) for x in range(0, 10)])

but, that is not the only new thing Brackets introduce. Brackets has a function
template that can be formatted just like Python strings:

.. code-block:: java

    template = def {
      while ({0}){
          {0} -= 1;
          print({0});
      }
    }

    func = template.format(10)
    func()

of-course no indent is needed, this is only done to make it *beautiful*. But,
that's not all that Brackets adds for functions, we have a ``?()`` for some
special cases. In ``something?(args, kwargs)`` for example, if ``something`` is
callable, it will be called, otherwise it will be passed as a variable:


.. code-block:: java

  y = 10
  print(y?(3, mul=10))

  def y(i, mul=1):
      return (i+3) * mul

  print(y?(3, mul=10))

where the first ``y?()`` returns 10, but the second one returns 60.
