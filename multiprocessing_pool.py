# Multiprocessing Process vs Pool
# Pool is most useful for large amounts of processes where each process can execute quickly, 
# while Process is most useful for a small number of processes where each process would take 
# a longer time to execute.

#Pool
# To use the Pool class, we also have to create a separate function that takes a list item as an argument like 
# we did when using Process. Then, using the multiprocessing module, create a Pool object called pool. 
# This object has a function called map, which takes the function we want to multiprocess and the list as arguments and 
# then iterates through the list for that function. After calling the function map, 
# close the object to allow for a clean shutdown.

import time
import multiprocessing 

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'

def multiprocessing_func(x):
    y = x**2
    time.sleep(1)
    print('{} squared results in a/an {} number for original number {}'.format(x, basic_func(y), y))
    
if __name__ == '__main__':
    
    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(0,10))
    pool.close()
    print('That took {} seconds'.format(time.time() - starttime))
    
#OUTPUT
# 0 squared results in a/an zero number of 0
# 1 squared results in a/an odd number of 1
# 2 squared results in a/an even number of 4
# 3 squared results in a/an odd number of 9
# 4 squared results in a/an even number of 16
# 5 squared results in a/an odd number of 25
# 6 squared results in a/an even number of 36
# 7 squared results in a/an odd number of 49
# 8 squared results in a/an even number of 64
# 9 squared results in a/an odd number of 81
# That took 5.032037258148193 seconds
