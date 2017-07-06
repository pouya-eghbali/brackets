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

