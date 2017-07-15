from brackets.translate import translate
import brackets.importer as importer
import brackets.runtime as runtime
import builtins as __builtins__

__version__ = '0.5.3'
__author__  = 'Pooya Eghbali [persian.writer at gmail]'

def eval(code, *args, **kwargs):
    try:
        code = translate(code)
    except:
        pass
    return __builtins__.eval(code, *args, **kwargs)

def exec(code, *args, **kwargs):
    try:
        code = translate(code)
    except:
        pass
    return __builtins__.exec(code, *args, **kwargs)

def compile(code, *args, **kwargs):
    try:
        code = translate(code)
    except:
        pass
    return __builtins__.compile(code, *args, **kwargs)
