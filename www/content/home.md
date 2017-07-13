---
title: "Home"
date: 2017-07-13T23:04:31+04:30
draft: true
---

<div id="home-slider">
  <div class="slide">
    <div class="description center">
      Bringing Brackets to Python
    </div>
    <div class="code">
      <pre><code class="hljs python">def fib(n) {
    a, b = 0, 1
    while (a < n) {
        print(a, end=' ')
        a, b = b, a+b
    }
    print()
}
      </code></pre>
    </div>
  </div>
  <div class="slide">
    <div class="description center">
      Powerful anonymous functions
    </div>
    <div class="code">
      <pre><code class="hljs python">print([def(x) {
        if(x in [0, 1]) {
          return x
        };
        while (x < 100) {
          x = x ** 2
        };
        return x
      }(x) for x in range(0, 10)])
      </code></pre>
    </div>
  </div>
  <div class="slide">
    <div class="description center">
      Extends keyword for classes
    </div>
    <div class="code">
      <pre><code class="hljs python">class Dog(name, breed) extends Animal(name) {
    def extend(self, name, breed) {
	    self.breed = breed
	}
    def woof(self) {
	    print("woof woof!")
	}
}
      </code></pre>
    </div>
  </div>
  <div class="slide">
    <div class="description center">
      Function Templates
    </div>
    <div class="code">
      <pre><code class="hljs python">template = def {
    while ({0}){
        {0} -= 1;
        print({0});
    }
}

func = template.format(10)
func()
      </code></pre>
    </div>
  </div>
  <div class="slide">
    <div class="description center">
      Template literals
    </div>
    <div class="code">
      <pre><code class="hljs python">x, y = 2, 10
print(`x is {x} and y is {x}, soooo x * y is {x * y}`)
      </code></pre>
    </div>
  </div>
  <div class="slide">
    <div class="description center">
      Regex support
    </div>
    <div class="code">
      <pre><code class="hljs perl">/^hel+o+$/i.match('HeLlLloOoOoOo')
'HeLlLloOoOoOo' =~ /^hel+o+$/i
// replacing:
(('HeLlLloOoOoOo' ~= /o/O/u) ~= /l/L/) ~= /e/E/
      </code></pre>
    </div>
  </div>
</div>

<script>
  $(function() {
    $("#home-slider").responsiveSlides({
        timeout: 8000,
        pager: true,
      });
  });
</script>

Brackets is a yet-another, a not just a pre-processor, a language built on top
of Python, allowing to use {} instead of indentation in Python, and it allows
defining powerful anonymous functions and introduces much more sugar and candy
into Python's syntax and abilities.

Installation is easy, choose a proper [Python](http://python.org) distribution
like [Anaconda](https://www.continuum.io/downloads), then run:

```
pip install brackets
```

* [Read the docs](http://docs.python-brackets.org)
* [Github](https://github.com/pooya-eghbali/brackets)
* [Brackets on PyPI](https://pypi.python.org/pypi/brackets)
