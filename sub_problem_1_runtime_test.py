import time
import find_attractors as sp1
import random
#from random_function import random_function

def random_function(degree):
    """Generates a random function in n variables"""
    function = [0] * 2 ** degree
    for i, _ in enumerate(function):
        function[i] = random.randint(0, 1)
    return function

a = [random_function(10) for i in range(10)]
start = time.time()
sp1.get_attractors_and_bassinets(a)
end = time.time()
print end-start