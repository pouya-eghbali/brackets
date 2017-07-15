from setuptools import find_packages, setup

setup(
    name='brackets',
    version='0.5.4',
    author='Pooya Eghbali',
    author_email='persian.writer@gmail.com',
    packages=find_packages(),
	package_data={
        'brackets.tests': ['*.bpy'],
    },
    url='http://python-brackets.org',
    license='BSD',
    description="""Use curly braces instead of indenting, plus much more sugar added to Python's syntax.""",
    classifiers= ['Intended Audience :: Developers',
                  'License :: OSI Approved :: BSD License',
                  'Operating System :: OS Independent',
                  'Programming Language :: Python :: 3'],
    entry_points = {
        'console_scripts': [
            'brackets=brackets.shell:main',
            'bpy-compile=brackets.compile:main',
        ],
    },
    keywords = 'brackets, indentation, indent, indenting, parser, encoding',
    platforms = ["Any"],
    long_description=open('README.txt').read(),
    install_requires=['yapf','regex'],
)
