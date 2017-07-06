import codecs, encodings
from encodings import utf_8
import regex as re
from random import randrange

__version__ = '0.2.0'
__author__  = 'Pooya Eghbali [persian.writer at gmail]'

def translate(a):

    create_matcher    = lambda keyword: re.compile(keyword + r'\s*(?<paren>\((?:[^()]++|(?&paren))*\))\s*(?<bracket>{(?:[^{}]++|(?&bracket))*})', flags=re.VERBOSE)
    while_matcher     = create_matcher('while')
    for_matcher       = create_matcher('for')
    if_matcher        = create_matcher('if')
    def_matcher       = create_matcher('def\s*(?<name>[^(]+?)')
    lambda_matcher    = create_matcher('def\s*')
    template_matcher  = re.compile(r'def\s*(?<bracket>{(?:[^{}]++|(?&bracket))*})', flags=re.VERBOSE)
    with_matcher      = create_matcher('with')
    string_matcher    = lambda x: re.search('""".*?"""'+"|'''.*?'''"+'|".*?"'+"|'.*?'",x,re.DOTALL)
    bracket_matcher   = re.compile(r'(?<bracket>{(?:[^{}]++|(?&bracket))*})', flags=re.VERBOSE)

    #Grab all the string literals:

    unique_slash_replacer          = '%030x' % randrange(16**50)
    unique_double_slash_replacer   = '%030x' % randrange(16**50)

    a = (a.replace("\\'", unique_slash_replacer)
          .replace('\\"', unique_double_slash_replacer))

    replaced_strings = {}

    while (string_matcher(a)):
        string =  (string_matcher(a)).span()
        
        unique_replacer = '%030x' % randrange(16**50)
        while unique_replacer in replaced_strings:
            unique_replacer = '%030x' % randrange(16**50)
        
        replaced_strings[unique_replacer] = a[string[0]:string[1]]
        a = a[:string[0]] + '-*'+unique_replacer+'*-\n' + a[string[1]:]

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

    # find and pew pew ifs:

    match = if_matcher.search(a)
    while match:
        start, end = match.span()
        code = 'if ' + match.group('paren')[1:-1] + ':' + match.group('bracket')[1:-1]
        a = a[:start] + code + a[end:]
        match = if_matcher.search(a)

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
        variables = set(v.strip() for v in re.findall(r'{\s*([^,}]+?)\s*}', code[1:-1], re.MULTILINE))
        args = '({0})'.format(', '.join('__{0}__'.format(v) for v in variables))
        code = '{' + re.sub(r'\n +{\s*([^,}]+?)\s*}\n\s+', r'__\1__', code[1:-1]) + '}'
        code = 'def ' + args + code
        code = '{0} = BracketsTemplateCreator({1})'.format(name, code)
        a = code + '\n' + a[:start] + name + a[end:]
        match = template_matcher.search(a)

    if tplrntm:
        a = 'from brackets.runtime import BracketsTemplateCreator, BracketsTemplate\n' + a

    # find and pew pew lambdas:

    match = lambda_matcher.search(a)
    while match:
        start, end = match.span()
        name = 'lambda_%030x' % randrange(16**50)
        code = 'def ' + name + match.group('paren') + ':' + match.group('bracket')[1:-1]
        a = code + a[:start] + name + a[end:]
        match = lambda_matcher.search(a)

    # put back the strings?

    for string in replaced_strings:
        a = a.replace('-*'+string+'*-', replaced_strings[string])

    # fix escapes?

    a = (a.replace(unique_slash_replacer,"\\'")
          .replace(unique_double_slash_replacer,'\\"'))

    # fix empty lines with indent?

    a = re.sub(' +\n', '\n', a)

    # fix double empty lines?

    a = re.sub('\n\n\n', '\n', a)

    # fix dictionaries?

    a = re.sub('\n}', '}', a)
    a = re.sub('\n{\n', '{', a)
    
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

