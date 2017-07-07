# coding: brackets

/*
this is just a
multiline comment :)
*/

x, y = 10, 12

print(`x is {x} and y is {y} and x + y is {x + y}`)

print([def(x, y) {return x + y}(x, y) for x in range(0, 5) for y in range(-5, 0)])
print([def(x) { if(x in [0, 1]) {return x}; while (x < 100) { x = x ** 2} return x}(x) for x in range(0, 10)])

print([def(x){
        if(x in [0, 1]) {
          return x
        };
        while (x < 100) {
          x = x ** 2
        };
        return x
      }(x) for x in range(0, 10)])

template = def {
    while ({0}){
        {0} -= 1;
        print({0});
    }
}

func = template.format(10)
func()

hello = def {
    print(`(Hello {{0}})`)
}

hello.format('Pouya')()

x = 10

if (x > 10) {
    print('x is > 10')
} else {
    print('x is not > 10')
}

if (True) {
if (x > 10) {
    print('x is > 10')
} elif (x == 10) {
    print('x is == 10')
} else {
    print('x is not > 10')
}
}

try {1 / 0}
except { print('exception happened') }

try {1 / 0}
except (ZeroDivisionError) {
    print('ZeroDivisionError happened')
}

class Test(object){
    def __init__(self) {
        print('Just testing classes');
    }
}

a = Test()

class Test{def __init__(self){print('Just testing the other classes');}}

a = Test()
