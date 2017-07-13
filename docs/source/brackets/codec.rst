Codec Approach
==============

On importing Brackets from Python interpreter, Brackets will register a codec
to Python's codecs system. You can use ``brackets.translate`` to translate a
code from Brackets syntax to Python's::

  import brackets
  brackets.translate("if(True){print('Yay!')}")

or you may decode a bytes object::

  b'if(True){print('Yay!')}'.decode('brackets')

or, because Brackets is a codec, you can create a .py file, write the magic
encoding comment::

    # coding: brackets

at top of this file, and then start coding in Brackets. You cannot run this file
directly with the Python interpreter, either it should be run with Brackets
interpreter or you should import it in another Python file after importing
Brackets::

    import brackets
    import my_file
