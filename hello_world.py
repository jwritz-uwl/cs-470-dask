from dask import delayed
from time import sleep

# Can change sleep times to see ordering

def say_hello():
    sleep(1)
    print("Hello")
    return 'hello'

def say_world():
    sleep(1)
    print("World")
    return 'world'

def say(x, y):
    sleep(1)
    print(x + y)

# These run immediately, all it does is build a graph
x = delayed(say_hello)()
y = delayed(say_world)()
z = delayed(say)(x, y)

print('Hello World!')

# This actually runs our computation using a local thread pool
z.compute()