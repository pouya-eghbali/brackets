import regex as re
import sys, traceback

def exception_handler(e, f, o):
    # e is the exception
    # f is translated file with debug info
    # o is the original file

    exc_type, exc_obj, exc_tb = sys.exc_info()

    while exc_tb.tb_next:
        exc_tb = exc_tb.tb_next

    frame  = exc_tb.tb_frame

    if hasattr(frame.f_code, 'co_filename'):
        file = frame.f_code.co_filename
    else:
        file = frame.f_code.co_name

    lineno = exc_tb.tb_lineno

    line = f[lineno-1]
    pos  = re.search(r'debug\((\d+),(\d+)\)', line)
    if not pos:
        raise e

    pos = int(pos.group(1))
    message = 'Error in:\n\n'
    curr_line = o[:pos].count('\n') + 1 + 1 # +1 because start line has no \n
                                            # +1 because starts at next line?
    lines = o.split('\n')

    index_line = curr_line - 1

    chunk = ''
    if index_line > 0:
        chunk += lines[index_line-1] + '\n'
    chunk += lines[index_line]
    if index_line < len(lines)-1:
        chunk += '\n' + lines[index_line+1]

    message += ('...\n' + chunk + '\n...\n\n\n')
    message += 'Error happened at position ' + str(pos) + ', line ' + str(curr_line) + ', file ' + file

    traceback.print_exc()
    print(exc_type(message), file=sys.stderr)
    sys.exit(1)
