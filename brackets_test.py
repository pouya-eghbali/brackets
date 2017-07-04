# coding: brackets

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