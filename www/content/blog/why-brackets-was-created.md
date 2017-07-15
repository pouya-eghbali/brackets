+++
date = 2017-07-15T18:46:40+04:30
tags = ["brackets", "history"]
title = "Why Brackets Was Created"
description = "Why Brackets Was Created"
author = "Pouya Eghbali"
draft = false
+++

There are a lot of programmers complaining about usage of white-spaces as
keywords and forcing indentation in Python, there are a lot of programmers who
prefer curly braces over indenting, that's it, for no reason, it's just their
taste, but, why did Brackets was created?

It was 2014, when I heard a friend complaining about Python and criticizing,
saying he will never use Python because of indenting, so I did a really small
Python codec to allow people use curly braces in their code, I published this
module on PyPI and put a DO NOT USE IT line in the readme. I considered it a
stupid idea, I preferred indenting over curly braces for various reasons.

So, why again, in 2017, I started working on this? People close to me know that
it's been years that I'm working on nlp software, and I was translating human
language to code (What a stupid idea, right? Oh well, not really), anyways,
back when I started that nlp software, I was working alone, and it was just at
early research stages, I tried a lot of programming languages, and a lot of
algorithms for this.

When working alone, I didn't care much about the syntax of the language, I loved
Lisp, I loved Python and I used Hy in my project. But, starting to work with
people, I figured Lisp wasn't a good choice. It was confusing for people, Lisp
is a great language, minimalistic at its syntax, highly suitable for what I
wanted to do, but some people aren't easy with it and I understand them.

I needed a language, functional, like Lisp, with ability to treat code as data,
and data as code, a language where blocks of code were well defined and could be
inserted at any place without any problems, like how it is possible to insert a
lisp block into another one, I needed a language where I could define anonymous
functions, powerful ones, like JavaScript, not like Python's lambdas, I needed
a sane language, where I could extend classes, instead of sub-classing just to
add a method to the class, and I needed all of the awesomeness of Python and
available modules and libraries.

Python, wasn't suitable for this task, just because it used indenting instead of
curly braces, so, that reminded me of my 2014 project, I forked the project and
started working on it, to make it suitable for this project. Purpose of this
project is to provide a functional Python, with curly braces, and easier syntax
for doing day to day tasks (that's why I added regex literals).

We're now using Brackets to develop our nlp software and we're satisfied with
it, and we're working to make Brackets better everyday. It is true that with
extending classes we're just sub-classing the parent again, and our powerful
anonymous functions aren't anonymous for real, but this works, and we're going
to solve all these problems in future.

Here's a piece of code from our nlp software:

```
_.each(charmap, def(la, fa, charmap, i){
    class transform_char() extends Transform(".*?%s.*?|%s"%(fa,fa)) {
        def process(self, cell){
            word = re.sub(fa, la, cell.text)
            return [Cell(word, {'word': word})]
        }
    }
    bridge.add_transform(transform_char())
})
```

And to include code blocks inside another code block we just had to do:

```
(def {
    return {0}?() + {1}?()
}).format(2, (def {
    return {0}?() ** 2
}).format(3))()
```
