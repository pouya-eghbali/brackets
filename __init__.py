import codecs, encodings
from encodings import utf_8
import re
from random import randrange

__version__ = '0.2.0'
__author__  = 'Pooya Eghbali [persian.writer at gmail]'

def translate(a):

    #;

    semicolons = [i.start() for i in re.finditer(';',a) if not
                  i in re.finditer('".*;.*"',a)]
    a = list(a)
    for semicolon in semicolons:
        indent = 0
        for i in (''.join(a)[:semicolon]).split('\n')[-1]:
            if i == ' ': indent+=1;continue
            break
        a[semicolon] = '\n'+' '*indent
    a = ''.join(a)

    #Grab all the string literals:

    unique_slash_replacer          = '%030x' % randrange(16**50)
    unique_double_slash_replacer   = '%030x' % randrange(16**50)

    a = (a.replace("\\'", unique_slash_replacer)
          .replace('\\"', unique_double_slash_replacer))

    replaced_strings = {}

    while (  re.search('""".*?"""',a,re.DOTALL)
          or re.search("'''.*?'''",a,re.DOTALL)
          or re.search('".*?"',a,re.DOTALL)
          or re.search("'.*?'",a,re.DOTALL)):
        string =  (  re.search('""".*?"""',a,re.DOTALL)
                  or re.search("'''.*?'''",a,re.DOTALL)
                  or re.search('".*?"',a,re.DOTALL)
                  or re.search("'.*?'",a,re.DOTALL)).span()
        unique_replacer = '%030x' % randrange(16**50)
        while unique_replacer in replaced_strings:
            unique_replacer = '%030x' % randrange(16**50)
        replaced_strings[unique_replacer] = a[string[0]:string[1]]
        a = a.replace(a[string[0]:string[1]],'-*'+unique_replacer+'*-')

    #endof function

    #endof = lambda s,i=0,c=1:(c==0 and i-1
    #               or s[i] == '}'  and endof(s,i+1,c-1)
    #               or s[i] == '{'  and endof(s,i+1,c+1)
    #               or endof(s,i+1,c))                      #THIS DOES NOT WORK! RECURSION LIMIT.

    def endof(s,i,p=False):
        c = 1
        for j, char in enumerate(s[i:]):
            if char == ('}' if not p else ')'): c-=1
            elif char == ('{' if not p else '('): c+=1
            if c == 0: return i+j

    def startof(i):
        e = endof(a,i=i.end()+1,p=True)
        return a[e:].find('{')+e+1

    #{} Preprocess

    pattern = '}\W*(if|elif|else|for|while|def|with)\W'
    for j, i in enumerate(sorted(([i.start() for i in re.finditer(pattern,a)]))):
        a = a[:i+j]+'\n'+a[i+j:]

    a = a.replace('}','\n}')

    #if

    ifs = [(startof(i)-1, endof(a,i=startof(i))) for i in re.finditer(r'(\s*|{|})if\s*?\(',a)]
    for i,_if in enumerate(sorted(ifs,key=lambda x:x[0])):
        a=(a[:_if[0]+i*2]+':\3\n'+a[_if[0]+i*2+1:_if[1]+i*2]+'\n'+a[_if[1]+i*2+1:])

    lines = [(len((a[:_if[0]+i*2]).split('\n')),len((a[:_if[1]+1+i*2]).split('\n')))
             for i,_if in enumerate(sorted(ifs,key=lambda x:x[0]))]

    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()

    #elif

    elifs = [(startof(i)-1, endof(a,i=startof(i))) for i in re.finditer(r'(\s*|{|})elif\s*?\(',a)]

    for i,_elif in enumerate(sorted(elifs,key=lambda x:x[0])):
        a=(a[:_elif[0]+i*2]+':\3\n'+a[_elif[0]+i*2+1:_elif[1]+i*2]+'\n'+a[_elif[1]+i*2+1:])

    lines = [(len((a[:_elif[0]+i*2]).split('\n')),len((a[:_elif[1]+1+i*2]).split('\n')))
             for i,_elif in enumerate(sorted(elifs,key=lambda x:x[0]))]

    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '\1' in a[i] and a[i] or a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()

    #else

    elses = [(i.end()-1,endof(a,i=i.end())) for i in re.finditer(r'(\s*|{|})else\s*?{',a)]

    for i,_else in enumerate(sorted(elses,key=lambda x:x[0])):
        a=(a[:_else[0]+i*2]+':\3\n'+a[_else[0]+i*2+1:_else[1]+i*2]+'\n'+a[_else[1]+i*2+1:])

    lines = [(len((a[:_else[0]+i*2]).split('\n')),len((a[:_else[1]+1+i*2]).split('\n')))
             for i,_else in enumerate(sorted(elses,key=lambda x:x[0]))]

    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '\1' in a[i] and a[i] or a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()

    #while

    whiles = [(startof(i)-1, endof(a,i=startof(i))) for i in re.finditer(r'(\s*|{|})while\s*?\(',a)]

    for i,_while in enumerate(sorted(whiles,key=lambda x:x[0])):
        a=(a[:_while[0]+i*2]+':\3\n'+a[_while[0]+i*2+1:_while[1]+i*2]+'\n'+a[_while[1]+i*2+1:])

    lines = [(len((a[:_while[0]+i*2]).split('\n')),len((a[:_while[1]+1+i*2]).split('\n')))
             for i,_while in enumerate(sorted(whiles,key=lambda x:x[0]))]

    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '\1' in a[i] and a[i] or a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()

    #For

    fors = [(startof(i)-1, endof(a,i=startof(i))) for i in re.finditer(r'(\s*|{|})for\s*?\(',a)]

    pairs = [(i.end()-1,endof(a,i.end(),p=True)) for i in re.finditer(r'(\s*|{|})for\s*?\(',a)]
    a = list(a)
    for pair in pairs:a[pair[0]]=' ';a[pair[1]]='\5'
    a = ''.join(a)

    for i,_for in enumerate(sorted(fors,key=lambda x:x[0])):
        a=(a[:_for[0]+i*2]+':\3\n'+a[_for[0]+i*2+1:_for[1]+i*2]+'\n'+a[_for[1]+i*2+1:])

    lines = [(len((a[:_for[0]+i*2]).split('\n')),len((a[:_for[1]+1+i*2]).split('\n')))
             for i,_for in enumerate(sorted(fors,key=lambda x:x[0]))]
    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '\1' in a[i] and a[i] or a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()
    a = a.replace('\5','')

    #anonymous def

    _def   = re.search(r'([^\x01](\s*|{|}))def\s*\(',a)

    while _def:
        start, end   = _def.start()+len(_def.group(1)), endof(a,i=startof(_def)) + 1
        identifier   = '%030x' % randrange(16**50)
        name         = 'lambda_' + identifier
        code         = a[start:end].replace('def', 'def '+name, 1)
        a            = list(a)
        a[start:end] = list(name)
        a            = ''.join(a)
        a            = code + '\n\n' + a
        _def         = re.search(r'([^\x01](\s*|{|}))def\s*\(',a)

    #def

    defs = [(startof(i)-1, endof(a,i=startof(i))) for i in re.finditer(r'(?<!\x01)(\s*|{|})def\s*.*?\(',a)]

    for i,_def in enumerate(sorted(defs,key=lambda x:x[0])):
        a=(a[:_def[0]+i*2]+':\3\n'+a[_def[0]+i*2+1:_def[1]+i*2]+'\n'+a[_def[1]+i*2+1:])

    lines = [(len((a[:_def[0]+i*2]).split('\n')),len((a[:_def[1]+1+i*2]).split('\n')))
             for i,_def in enumerate(sorted(defs,key=lambda x:x[0]))]
    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '\1' in a[i] and a[i] or a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()

    #with

    withs = [(startof(i)-1, endof(a,i=startof(i))) for i in re.finditer(r'(\s*|{|})with\s*?\(',a)]

    pairs = [(i.end()-1,endof(a,i.end(),p=True)) for i in re.finditer(r'(\s*|{|})with\s*?\(',a)]
    a = list(a)
    for pair in pairs:a[pair[0]]=' ';a[pair[1]]='\5'
    a = ''.join(a)

    for i,_with in enumerate(sorted(withs,key=lambda x:x[0])):
        a=(a[:_with[0]+i*2]+':\3\n'+a[_with[0]+i*2+1:_with[1]+i*2]+'\n'+a[_with[1]+i*2+1:])

    lines = [(len((a[:_with[0]+i*2]).split('\n')),len((a[:_with[1]+1+i*2]).split('\n')))
             for i,_with in enumerate(sorted(withs,key=lambda x:x[0]))]
    a = a.split('\n')
    for line in sorted(lines, key = lambda x:x[0]):
        line = (line[0]-1,line[1])
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '\1' in a[i] and a[i] or a[i].strip()
    for line in sorted(lines, key = lambda x:x[0]):
        for i in range(0, len(a)):
            if i in range(*line):
                a[i] = '    '+a[i]+'\1'
    a = ('\n'.join(a)).rstrip()
    a = a.replace('\5','')

    #Fix \1 mark

    a = a.split('\n')
    for i in range(0, len(a)):
        if '\3' in a[i]:
            indents = len(a[i])-len(a[i].lstrip())
            a[i] = a[i].lstrip().replace('\3','')
            a[i] = ' '*(max([a[i+1].count('\1')-1, a[i].count('\1')])*4)+a[i]+'\1'*(a[i+1].count('\1')-1)
            a[i+1] = a[i+1].lstrip()
            a[i+1] = ' '*(a[i+1].count('\1'))*4+a[i+1]

    for i in range(0, len(a)):
        while '\1' in a[i]:
            a[i] = a[i].replace('\1','')

    #Fix empty lines:

    a = '\n'.join([l for l in a if l and not l.isspace()]).rstrip()

    #Fix }:

    while re.search('\s+}',a):
        result = re.search('\s+}',a)
        a = a.replace(a[result.start():result.end()],'}')

    #replace replaced strings

    for string in replaced_strings:
        a = a.replace('-*'+string+'*-', replaced_strings[string])

    a = (a.replace(unique_slash_replacer,"\\'")
          .replace(unique_double_slash_replacer,'\\"'))

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
