Regex
=====

There is support for regex literals, just like JavaScript and Perl, if you use
a regex literal in your code, regex module will be imported automatically as a
runtime dependency.

To define a regex pattern:

.. code-block:: perl

    my_compiled_pattern = /pattern/flags
    match_hello = /hello/i

these patterns are compiled and returned. Brackets uses `regex
<https://pypi.python.org/pypi/regex>`_ Python module. You can check its
documentation there. Available flags are:

* a, l, u for ASCII, LOCALE, UNICODE
* b, e for BESTMATCH, ENHANCEDMATCH
* p for POSIX
* r for REVERSE
* 0, 1 for VERSION0, VERSION1
* f, i for FULLCASE, IGNORECASE
* m, d, v, w for MULTILINE, DOTALL, VERBOSE, WORD

To match you can do:

.. code-block:: perl

    /^hel+o+$/i.match('HeLlLloOoOoOo')

or

.. code-block:: perl

    'HeLlLloOoOoOo' =~ /^hel+o+$/i

to replace you can do:

.. code-block:: perl

    (('HeLlLloOoOoOo' ~= /o/O/u) ~= /l/L/) ~= /e/E/

currently chaining =~ and ~= isn't supported but I'm planning to add support.
