import time

t1 = time.time()

for i in range(1000000):
    i ** 10

t2 = time.time()

elapsed_time = t2 - t1

print(elapsed_time)