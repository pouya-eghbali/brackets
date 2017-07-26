import builtins as __builtins__
from brackets.translate import translate

def eval(code, *args, **kwargs):
    code, debug, original = translate(code)
    try:
        return __builtins__.eval(code, *args, **kwargs)
    except Exception as e:
        exception_handler(e, debug, original)

def exec(code, *args, **kwargs):
    code, debug, original = translate(code)
    try:
        return __builtins__.exec(code, *args, **kwargs)
    except Exception as e:
        exception_handler(e, debug, original)

def compile(code, *args, **kwargs):
    code, debug, original = translate(code)
    try:
        return __builtins__.compile(code, *args, **kwargs)
    except Exception as e:
        exception_handler(e, debug, original)
