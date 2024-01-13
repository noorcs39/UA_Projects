import math
import numpy as np
import matplotlib.pyplot as plt

class MyApproxCounter:
    def __init__(self):
        self.my_val = 0
        
    def my_increment(self) -> int:
        my_delta = 1 / (self.my_get_val(self.my_val + 1) - self.my_get_val(self.my_val))
        my_random = np.random.uniform(0, 1)
        if my_random < my_delta:
            self.my_val += 1
        return self.my_val

    def my_get_val(self, v):
        return (math.e ** (math.log(2) * v)) - 1

MAX_ITERATIONS = 800

approx_values = []
my_counter = MyApproxCounter()
for iteration in range(MAX_ITERATIONS):
    my_n = iteration
    my_counter.my_increment()
    approx_values.append((my_n, my_counter.my_get_val(my_counter.my_val)))

plt.plot(list(range(MAX_ITERATIONS)), [x[0] for x in approx_values], label="Iterations ($n$)")
plt.plot(list(range(MAX_ITERATIONS)), [x[1] for x in approx_values], label="Approximate Values ($v$)")
plt.xlabel('Iterations')
plt.ylabel('Values')
plt.title('My Approximate Counter Simulation')
plt.legend()
plt.show()
