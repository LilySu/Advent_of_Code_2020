# lambda and dynamically named classes
# morphing classes that change throughout the runtime


def loop(func, condition, reeturn, **kwargs):
    while eval(condition):
        func()
    return eval(reeturn)

fib = type(
    'Fibonacci',
     (),
     {
         '_cache': [0, 1],
         '_construct': lambda self, n: loop(self._build, "len(kwargs['arr']) < kwargs['n']", "kwargs['arr'][-1]", n=n, arr=self._cache),
         '_build': lambda self: self._cache.append(self._cache[-1]+self._cache[-2]),
         # add end value for fibonacchi
         'at': lambda self, n: self._cache[n] if len(self._cache) >= n else self._construct(n),
    }
)

instance = fib()
print(instance.at(10))
print(instance._cache)
print(instance, type(instance))
print(dir(instance), instance.__dict__)


# class MyClass:
#   pass
#
# myClass = MyClass()
#
# e = MyClass
# a = e()
# print(a, myClass)

# # This works
# instance = Fibonacci()
# print(instance.at(7))
# print(instance._cache)
# print(instance, type(instance))
# print(dir(instance), instance.__dict__)


def loop(func, condition, reeturn, **kwargs):
    while eval(condition):
        func()
    return eval(reeturn)

my_class = "AppleSauce"

locals()[my_class ] = type(
    my_class,
     (),
     {
         '_cache': [0, 1],
         '_construct': lambda self, n: loop(self._build, "len(kwargs['arr']) < kwargs['n']", "kwargs['arr'][-1]", n=n, arr=self._cache),
         '_build': lambda self: self._cache.append(self._cache[-1]+self._cache[-2]),
         'at': lambda self, n: self._cache[n] if len(self._cache) >= n else self._construct(n),
    }
)

instance = eval(f"{my_class}()")
print(instance.at(7))
print(instance._cache)
print(instance, type(instance))
print(dir(instance), instance.__dict__)

# prototype - creating an object without a class
# javascript is a prototype-based language