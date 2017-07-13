Brackets Interpreter
====================

Brackets comes with its own shell and interpreter, to start Brackets shell, just
type ``brackets`` in your command line environment, terminal or console::

    brackets

this will bring up the Brackets shell, were you can write and execute Brackets
code. You can use and import any Python libraries and files you want. Remember,
all Brackets code is Python compatible and all Python code can run in Brackets.

If you don't pass a file name to ``brackets`` it will bring up the Brackets
shell, but if you give it a file name, it will execute that file for you::

    brackets hello.bpy

You can use ``-c`` option to run a command::

    brackets -c "print('Hello world!')"

You can use ``-i`` option to read from stdin, you can also pip stuff to brackets
::

    echo print('Hello world') | brackets

there's ``--spy`` option to spy on generated code, this will show generated code
before executing in Brackets shell.
