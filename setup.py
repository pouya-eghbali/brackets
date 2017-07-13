from setuptools import find_packages, setup

setup(
    name='brackets',
    version='0.4.1',
    author='Pooya Eghbali',
    author_email='persian.writer@gmail.com',
    packages=find_packages(),
	package_data={
        'brackets.tests': ['*.bpy'],
    },
    url='http://python-brackets.org',
    license='BSD',
    description="""Use {} instead of indenting, write powerful lambdas, and much more sugar added to Python's syntax and abilities.""",
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
