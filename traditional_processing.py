# The traditional for-loop iteration goes through the list one by one and performs the functions on each item individually. 
# In this model, the loops use only 30 to 40 percent of the available CPU power. If we were to use multiprocessing, 
# the function would be executed on multiple list items at once and up to 100 percent of the CPU could be used on a 
# multicore machine. Best of all, we would see a dramatic reduction in execution time.

# Traditional way

import time

def basic_func(x):
    if x == 0:
        return 'zero'
    elif x%2 == 0:
        return 'even'
    else:
        return 'odd'
    
starttime = time.time()
for n in range(0,10):
    y = n**2
    time.sleep(2)
    print('{} squared results in a/an {} number of {}'.format(n, basic_func(y), y))
    
print('That took {} seconds'.format(time.time() - starttime))
