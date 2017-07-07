import codecs, encodings
from encodings import utf_8
import regex as re
from random import randrange
from yapf.yapflib.yapf_api import FormatCode

__version__ = '0.3.3'
__author__  = 'Pooya Eghbali [persian.writer at gmail]'

def translate(a):

    create_matcher       = lambda keyword: re.compile(keyword + r'\s*(?<paren>\((?:[^()]++|(?&paren))*\))\s*(?<bracket>{(?:[^{}]++|(?&bracket))*})', flags=re.VERBOSE)
    create_np_matcher    = lambda keyword: re.compile(keyword + r'\s*(?<bracket>{(?:[^{}]++|(?&bracket))*})', flags=re.VERBOSE)
    while_matcher        = create_matcher('while')
    for_matcher          = create_matcher('for')
    if_matcher           = create_matcher('if')
    elif_matcher         = create_matcher('elif')
    try_matcher          = create_np_matcher('try')
    except_matcher       = create_matcher('except')
    except_np_matcher    = create_np_matcher('except')
    def_matcher          = create_matcher('def\s*(?<name>[^(]+?)')
    lambda_matcher       = create_matcher('def')
    template_matcher     = create_np_matcher('def')
    class_matcher        = create_matcher('class\s*(?<name>[^(]+?)')
    class_np_matcher     = create_np_matcher('class\s*(?<name>[^(]+?)')
    else_matcher         = create_np_matcher('else')
    with_matcher         = create_matcher('with')
    string_matcher       = lambda x: re.search('""".*?"""'+"|'''.*?'''"+'|".*?"'+"|'.*?'",x,re.DOTALL)
    comment_matcher      = lambda x: re.search(r"//.*?\n|/\*.*?(\*/)",x,re.DOTALL)
    bracket_matcher      = re.compile(r'(?<bracket>{(?:[^{}]++|(?&bracket))*})', flags=re.VERBOSE)
    literal_matcher      = lambda x: re.search(r"`.*?`",x,re.DOTALL)

    # replace all escapes oh well:

    unique_slash_replacer          = '%030x' % randrange(16**50)
    unique_double_slash_replacer   = '%030x' % randrange(16**50)
    unique_grave_slash_replacer    = '%030x' % randrange(16**50)

    a = (a.replace("\\'", unique_slash_replacer)
          .replace('\\"', unique_double_slash_replacer)
          .replace('\\`', unique_grave_slash_replacer))

    # pew pew template literals

    fstrlitrtm = False

    while (literal_matcher(a)):
        fstrlitrtm = True
        start, end = literal_matcher(a).span()
        literal = a[start:end]
        a = a[:start] + 'FormatStringLiteral("{0}", globals(), locals())'.format(literal[1:-1]) + a[end:]

    # pew pew all the strings

    replaced_strings = {}

    while (string_matcher(a)):
        string =  string_matcher(a).span()

        unique_replacer = '%030x' % randrange(16**50)
        while unique_replacer in replaced_strings:
            unique_replacer = '%030x' % randrange(16**50)

        replaced_strings[unique_replacer] = a[string[0]:string[1]]
        a = a[:string[0]] + '-*'+unique_replacer+'*-\n' + a[string[1]:]

    # well, i'll just remove the comments:

    while (comment_matcher(a)):
        start, end =  (comment_matcher(a)).span()
        a = a[:start] + a[end:]

    # ; means line-break, sooooo:

    a = re.sub(';\s*', '\n', a)

    # every } is a }; sooooo:

    a = re.sub('}\s*', '\n}\n', a)

    # and each { is beginning of a line:

    a = re.sub('{\s*', '\n{\n', a)

    # oki now indent EVERYTHING:

    match = bracket_matcher.search(a)
    while match:
        start, end = match.span()
        a = a[:start] + '\1' + '\n    '.join((a[start+1:end-1]).split('\n')) + '\2' + a[end:]
        match = bracket_matcher.search(a)

    a = a.replace('\1', '{')
    a = a.replace('    \2', '}')

    # find and pew pew whiles:

    match = while_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'while ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = while_matcher.search(a)

    # find and pew pew elifs:

    match = elif_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'elif ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = elif_matcher.search(a)

    # find and pew pew ifs:

    match = if_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'if ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = if_matcher.search(a)

    # find and pew pew elses:

    match = else_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'else:' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = else_matcher.search(a)

    # find and pew pew fors:

    match = for_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'for ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = for_matcher.search(a)

    # find and pew pew withs:

    match = with_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'with ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = with_matcher.search(a)

    # find and pew pew trys:

    match = try_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'try:' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = try_matcher.search(a)

    # find and pew pew excepts:

    match = except_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'except ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = except_matcher.search(a)

    match = except_np_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'except:' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = except_np_matcher.search(a)

    # find and pew pew classes:

    match = class_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'class ' + match.group('name') + match.group('paren') + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = class_matcher.search(a)

    match = class_np_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'class ' + match.group('name') + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = class_np_matcher.search(a)

    # find and pew pew defs:

    match = def_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'def ' + match.group('name') + match.group('paren') + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = def_matcher.search(a)

    # find and pew pew templates:

    match = template_matcher.search(a)
    tplrntm = bool(match)
    while match:
        start, end = match.span()
        name = 'template_%030x' % randrange(16**50)
        code =  match.group('bracket')
        variables = set(v.strip() for v in re.findall(r'{\s*([^{},]+?)\s*}', code[1:-1], re.MULTILINE))
        literals = re.finditer('FormatStringLiteral\(-\*(?<strname>.*?)\*-\s*,\s*globals\(\),\s*locals\(\)\)', code, re.MULTILINE)
        pattern = r'(\{(?>[^,{}]+|(?1))*\})'
        for literal in literals:
            string = replaced_strings[literal.group('strname')]
            outers = list(re.finditer(pattern, string))
            inners = [[outer, list(re.finditer(pattern, outer.group(0)[1:-1]))] for outer in outers]
            inners = [[i[0], j] for i in inners for j in i[1] if i[1] and j.group(0).count('{') == 1]
            inners = [[o.start()+i.start()+1,o.start()+i.end()+1, i.group(0)[1:-1].strip()] for o, i in inners]
            for inner in inners:
                string = string[:inner[0]] + '__{0}__'.format(inner[2]) + string[inner[1]:]
                variables.add(inner[2])
            replaced_strings[literal.group('strname')] = string
        args = '({0})'.format(', '.join('__{0}__'.format(v) for v in variables))
        code = '{' + re.sub(r'\n +{\s*([^,}]+?)\s*}\n\s+', r'__\1__', code[1:-1]) + '}'
        code = 'def ' + args + code
        code = '{0} = BracketsTemplateCreator({1})'.format(name, code)
        a = code + '\n' + a[:start] + name + a[end:]
        match = template_matcher.search(a)

    # find and pew pew lambdas:

    match = lambda_matcher.search(a)
    while match:
        start, end = match.span()
        name = 'lambda_%030x' % randrange(16**50)
        code = 'def ' + name + match.group('paren') + ':' + match.group('bracket')[1:-1]
        a = code + a[:start] + name + a[end:]
        match = lambda_matcher.search(a)

    # replace encoding thingy?

    a = re.sub('#\s*coding:\s*brackets', '', a)

    # put back the strings?

    for string in replaced_strings:
        a = a.replace('-*'+string+'*-', replaced_strings[string])

    # fix escapes?

    a = (a.replace(unique_slash_replacer,"\\'")
          .replace(unique_grave_slash_replacer,'`')
          .replace(unique_double_slash_replacer,'\\"'))

    # fix empty lines with indent?

    a = re.sub(' +\n', '\n', a)

    # fix double empty lines?

    a = re.sub('\n\n\n', '\n', a)

    # fix dictionaries?

    a = re.sub('\n}', '}', a)
    a = re.sub('\n{\n', '{', a)

    # import runtime thingies?

    if tplrntm:
        a = 'from brackets.runtime import BracketsTemplateCreator, BracketsTemplate\n' + a
    if fstrlitrtm:
        a = 'from brackets.runtime import FormatStringLiteral\n' + a

    # reformat code?

    a = FormatCode(a)[0]

    return a

def search_function(s):
    if s!='brackets': return None
    utf8=encodings.search_function('utf8') # Assume utf8 encoding
    def decode(memory):
        k = utf8.decode(memory)
        data = translate(k[0])
        return (data, len(data))
    return codecs.CodecInfo(
        name='brackets',
        encode = utf8.encode,
        decode = decode,
        incrementalencoder=utf8.incrementalencoder,
        incrementaldecoder=utf8.incrementaldecoder,
        streamreader=utf8.streamreader,
        streamwriter=utf8.streamwriter)

codecs.register(search_function)

if __name__ == '__main__':
    with open('brackets_test.py', 'rb') as f:
        print(f.read().decode('brackets'))
