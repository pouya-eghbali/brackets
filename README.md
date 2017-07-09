
# Brackets

Use js-style brackets instead of indentation. This is an encoding, you can also import this module in sites.py, it will register the encoding on import.

To install:

```
pip install brackets
```

to use this, add the magic encoding comment to your source file:

```
# coding: brackets
```

Then you can import it directly (obvsly brackets should be imported first), or if you added the encoding to your sites.py, you can use idle to view the decoded file.


Currently just works for "if|elif|else|for|while|def|with|try|except|class" statements, lambda, function templates, js-style template literals. It's also possible to mix indentation and brackets. You can do that, but it is not recommended.
This started as a code, a hobby project in 2014, but now I started working on it again, and I rewrote it completely.

You can also decode brackets literals:

```
import brackets
a = b'brackets code'
a.decode('brackets')
```

or translate:

```
brackets.translate(code) # utf8 string
```

To know how to code with brackets examine the examples provided here. There's no warranty. There might be parsing errors, report if there are any, feel free to make a pull request.

## What this can do?

This will convert:

```
if(1 in {1,2,3}){
    print(5)
    for(x in c){
        print(c)
    }
}
```

To this:

```
if(1 in {1,2,3}):
    print(5)
    for x in c:
        print(c)
```

It works for messy code too. see how this can work on this one-line code:

```
def fib(n){if(n in 0){return n}else{return fib(n-1)+fib(n-2)}}
```

The result from the previous is:

```
def fib(n):
    if(n in 0):
        return n
    else:
        return fib(n-1)+fib(n-2)
```

using ; is supported:

```
import io; def fib(n){/* code */} ; print("hello");
```

js-style comments are supported:
```
/* this is a
   multiline
   comment   */
```

You can also write anonymous functions like this:

```
print([def(x, y) {return x + y}(x, y) for x in range(0, 5) for y in range(-5, 0)])
print([def(x) { if(x in [0, 1]) {return x}; while (x < 100) { x = x ** 2} return x}(x) for x in range(0, 10)])
```

Not necessarily in one line:

```
print([def(x) {
        if(x in [0, 1]) {
          return x
        };
        while (x < 100) {
          x = x ** 2
        };
        return x
      }(x) for x in range(0, 10)])
```

Note that this anonymous function isn't Python lambda, they're real functions, without limitations of lambda.

There's support for function templates, they can be formatted the same way as strings are formatted, you cannot insert new code unless you're formatting them with a function:

```
template = def {
    while ({0}){
        {0} -= 1;
        print({0});
    }
}

func = template.format(10)
func()
```
Js-style template literals are also available:

```
x, y = 2, 10
print(`x is {x} and y is {x}, soooo x * y is {x * y}`)
```

Add ? before an object's () to execute them only if they're callable, otherwise just to assume its value:

```
y = 10
print(y?(3, mul=10)) # will print 10

def y(i, mul=1):
    return (i+3) * mul

print(y?(3, mul=10)) # will print 60
```

## Project Info

Github project page: https://github.com/pooya-eghbali/brackets
Mail me at: persian.writer [at] Gmail.com
