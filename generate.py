import pypandoc
long_description = pypandoc.convert_file('README.md', 'rst', outputfile="README.txt")