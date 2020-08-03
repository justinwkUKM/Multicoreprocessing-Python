# The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously.
# ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global Interpreter Lock
# but also means that only picklable objects can be executed and returned.
# ThreadPoolExecutor class implements Threading instead of Multiprocessing
import concurrent.futures
import time

start = time.perf_counter()


def do_a_task(seconds) -> str:
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'

# THE WITH FUNCTION acts as a context manager. Auto joins all the processes
# '''submit many processes'''
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(do_a_task, 2) for i in range(10)]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#         # returns the object


'''submit many processes with varying times'''
# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     # list(reversed(secs))
#     results = [executor.submit(do_a_task, sec) for sec in secs]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#         # returns the object

'''map function maps the whole list to the function and simply return the result. Map returns result as the 
processes were started (order) not as they were completed.'''
with concurrent.futures.ProcessPoolExecutor() as executor:
    # val = executor.submit(do_a_task, 5)
    secs = list(reversed([i for i in range(1, 6)]))
    results = executor.map(do_a_task, secs)

    for res in results:
        print(res)

finish = time.perf_counter()

print(f'finished in {round(finish-start, 2)} second(s)...')
