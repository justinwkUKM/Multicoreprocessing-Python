# Multiprocessing Process vs Pool
# Pool is most useful for large amounts of processes where each process can execute quickly, 
# while Process is most useful for a small number of processes where each process would take 
# a longer time to execute.

#Process
# The Process class sends each task to a different processor, and the Pool class sends sets of tasks to different processors. 
# To use the Process class, place the functions and calculations that are done on each list item in its own function that will 
# take a list item as one of its arguments. Next, import the multiprocessing module, create a new process for each list item, 
# and trigger each process in one call. We keep track of these processes by making a list and adding each process to it. 
# After creating all the processes, take the separate output of each CPU and join them into a single list.


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
    time.sleep(5)
    print('{} squared results in a/an {} number of {}'.format(x, basic_func(y), y))
    
if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(0,10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()
        
    for process in processes:
        process.join()
        
    print('That took {} seconds'.format(time.time() - starttime))