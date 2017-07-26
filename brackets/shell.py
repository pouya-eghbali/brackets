import code
import brackets
import sys
import argparse
import brackets.importer
from brackets.helpers import eval, exec, compile
from brackets import exception_handler

USAGE = "%(prog)s [-h | -c cmd | file | -] [arg] ..."
VERSION = "%(prog)s " + brackets.__version__
EPILOG = """  file         program read from script
  -            program read from stdin
  [arg] ...    arguments passed to program in sys.argv[1:]
"""
BANNER = "Brackets %s\nRunning Python %s on %s\n" % (brackets.__version__, sys.version, sys.platform)

class Console(code.InteractiveConsole):
    def __init__(self, spy=False, source='', *args, **kwargs):
        self.spy = spy
        super().__init__(*args, **kwargs)
        self.runsource('from brackets import *')
        if source:
            self.runsource(source)

    def runsource(self, source, filename="<input>", symbol="single"):
        try:
            code, debug, original = brackets.translate(source)
        except:
            if source.endswith('\n'):
                # Case 1
                self.showsyntaxerror(filename)
                return False
            else:
                return True

        if code is None:
            # Case 2
            return True

        # Case 3
        if self.spy:
            print(('-'*80)+'\n{0}'.format(code)+('-'*80))
        self.runcode(code)
        return False

def shell(scriptname, argv):
    parser = argparse.ArgumentParser(
        prog="brackets",
        usage=USAGE,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=EPILOG)

    parser.add_argument("-c", dest="command",
                        help="program passed in as a string")

    parser.add_argument("--spy", action="store_true",
                        help="print equivalent Python code before executing")

    parser.add_argument("-v", "--version", action="version", version=VERSION)


    # this will contain the script/program name and any arguments for it.
    parser.add_argument('args', nargs=argparse.REMAINDER,
                        help=argparse.SUPPRESS)

    # stash the brackets executable in case we need it later
    # mimics Python sys.executable
    brackets.executable = argv[0]

    options = parser.parse_args(argv[1:])

    # reset sys.argv like Python
    sys.argv = options.args

    if options.command:
        # User did "brackets -c ..."
        return run_command(options.command)

    if options.args:
        if options.args[0] == "-":
            # Read the program from stdin
            return run_command(sys.stdin.read())

        else:
            # User did "brackets <filename>"
            return run_file(options.args[0])

    # User did NOTHING!
    return run_repl(spy=options.spy)

def run_repl(spy):
    sys.exit(Console(spy).interact(banner=BANNER))

def run_command(command):
    code, debug, original = brackets.translate(command)
    try:
        sys.exit(Console().runcode(code))
    except Exception as e:
        exception_handler(e, debug, original)

def run_file(file):
    brackets.importer.BracketsLoader('__brackets_main__', file).load_module('__brackets_main__')

def main():
    sys.exit(shell("brackets", sys.argv))

if __name__ == '__main__':
    main()
