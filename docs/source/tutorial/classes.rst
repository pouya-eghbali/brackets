Classes
=======

Brackets brings the ``{}`` to classes too:

.. code-block:: java

  class Animal(object) {
    def __init__(self, name) {
      self.name = name
    }
    def hi(self) {
      print("hi, my name is {0}".format(self.name))
    }
  }

but, Brackets, also brings ``extends`` keyword to Python:

.. code-block:: java

  class Dog(name, breed) extends Animal(name) {
    def extend(self, name, breed) {
      self.breed = breed
    }
    def woof(self) {
      print("woof woof!")
    }
  }

Code block above defines a class Dog, that inherits from Animal, class Dog
requires name and breed, these will be passed to Dog's ``__init__`` function,
and name, will be passed to ``super().__init__`` function. Note that you may
pass anything to ``super()`` you're not limited to arg names like ``name``:

.. code-block:: java

  class Shepherd(name) extends Dog(name, "Shepherd") {}

These new classes will have an ``__init__`` function, that is generated
automatically by Brackets, you can define a ``extend`` function just like the
code examples above, it will be called inside auto-generated ``__init__`` after
``super`` stuff and all of the args in super will be passed to it. This way,
it's exactly like class definitions in Python that inherit from other class:

.. code-block:: js

  class Cat(name) extends Animal(name) {
    def meow(self) {
      print("meow!")
    }
  }

  dog = Dog('Bailey', 'Shepherd')
  dog.hi()
  dog.woof()

  cat = Cat('Smokey')
  cat.meow()

you can also define classes by extending ``object`` class if you prefer that:

.. code-block:: java

  class whatever() extends object() {}
