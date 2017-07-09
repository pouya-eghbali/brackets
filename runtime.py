import sys
import regex as re

class BracketsTemplateCreator(object):
    """
    def {
        print({0} + {1});
        print({keyword});
    }
    """
    def __init__(self, callable):
        self.callable = callable

    def format(self, *args, **kwargs):
        format = {}
        for index, arg in enumerate(args):
            format['__{0}__'.format(index)] = arg
        format.update(kwargs)
        return BracketsTemplate(self.callable, format)

class BracketsTemplate(object):
    def __init__(self, callable, format):
        self.callable = callable
        self.format   = format

    def __call__(self):
        return self.callable(**self.format)

def FormatStringLiteral(string, globals, locals):
    matcher = re.compile('\{.*?\}')
    match   = matcher.search(string)
    while match:
        start, end = match.span()
        code = string[start:end]
        val  = eval(code[1:-1], globals, locals)
        string = string[:start] + str(val) + string[end:]
        match   = matcher.search(string)
    return string

def ConditionalFunctionCall(function, *args, **kwargs):
    if callable(function):
        return function(*args, **kwargs)
    return function
