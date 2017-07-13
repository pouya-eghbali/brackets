Flow Control
============

Let's start by syntax changes, basically, instead of indenting and ``:`` use
``()`` and ``{}``, so this::

    if expression:
        do whatever

becomes:

.. code-block:: java

    if(expression){
        do whatever
    }

there is no need for indenting there of-course. Either separate lines by a
``\n`` (new line) character, or by a ``;``, they're equivalent in Brackets:

.. code-block:: java

    line one; line two; line ...;

for example you can write:

.. code-block:: java

    if(expression) {
       print("Hello world!"); print("Brackets are awesome!")
    }

so that's that, there's the same syntax for other stuff too:

.. code-block:: java

    if(expression) {
       whatever...
    } elif (other thingy) {
       do other whatever!
    } else {
       oh well nothing matched?
    }

the same syntax for ``for`` and ``while``:

.. code-block:: java

    while(expression) {
       what should be looped?
    }

    for(whatever) {
       do something to whatever
    }

same simple syntax for ``with``, ``try`` and ``except``:

.. code-block:: java

    with (open(file) as f) {
       do something to this file
    }

and to catch exceptions:

.. code-block:: java

    try {
       something
    } except {
       oh something went wrong!
    }

    try {
       some other thing
    }
    except (thatException) {
       oh wow it failed because thatException!
    }
