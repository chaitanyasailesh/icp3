import numpy as np
import random
x = np.random.randint(1, 20, 15)
print("Original array:"+str(x))
max_value = x.max()
print("maximum value is"+str(max_value))
index = x.argmax()
x[index] = 0
print("output"+str(x))


