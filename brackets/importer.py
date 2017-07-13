import sys
from importlib.machinery import FileFinder
import importlib.util
import os.path, os
from brackets import translate
import marshal

def write_code_as_pyc(st, cfile, code):
    
    from importlib.util import MAGIC_NUMBER as MAGIC  # NOQA

    def wr_long(f, x):
        """Internal; write a 32-bit int to a file in little-endian order."""
        f.write(bytes([x & 0xff,
                       (x >> 8) & 0xff,
                       (x >> 16) & 0xff,
                       (x >> 24) & 0xff]))

    timestamp = int(st.st_mtime)

    try:
        os.makedirs(os.path.dirname(cfile))
    except (IOError, OSError):
        pass

    with open(cfile, 'wb') as fc:
        fc.write(MAGIC)
        wr_long(fc, timestamp)
        wr_long(fc, st.st_size)
        marshal.dump(code, fc)

class BracketsLoader(object):
    def __init__(self, name, path):
        self.path = path
    def load_module(self, fullname):
        
        if fullname in sys.modules:
            return sys.modules[fullname]
        
        cache_path = os.path.join(os.path.dirname(self.path), '__pycache__')
        cache_name = os.path.basename(self.path).rstrip('bpy')+'pyc'
        cache_file = os.path.join(cache_path, cache_name)
        
        if os.path.exists(cache_file):
            cache_time = os.path.getmtime(cache_file)
            cache_load = cache_time >= os.path.getmtime(self.path)
            
        if not os.path.exists(cache_file) or not cache_load:
            with open(self.path, 'r', encoding='utf8') as f:
                source = f.read()
            source = translate(source)
            code = compile(source, self.path, 'exec')
            st   = os.stat(self.path)
            write_code_as_pyc(st, cache_file, code)

        spec = importlib.util.spec_from_file_location(
                    fullname, cache_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[fullname] = module
        return module

class BracketsImporter(object):
    def find_on_path(self, fullname):
        fls = ["%s/__init__.bpy", "%s.bpy"]
        dirpath = "/".join(fullname.split("."))

        for pth in sys.path:
            pth = os.path.abspath(pth)
            for fp in fls:
                composed_path = fp % ("%s/%s" % (pth, dirpath))
                if os.path.exists(composed_path):
                    return composed_path

    def find_module(self, fullname, path=None):
        path = self.find_on_path(fullname)
        if path:
            return BracketsLoader(fullname, path)

sys.meta_path.insert(0, BracketsImporter())
sys.path.insert(0, "")

#brackets_hook = FileFinder.path_hook( (BracketsLoader, ['.bpy']) )
#sys.path_hooks.insert(0, brackets_hook)
# Need to invalidate the path hook's cache and force reload
#sys.path_importer_cache.clear()
