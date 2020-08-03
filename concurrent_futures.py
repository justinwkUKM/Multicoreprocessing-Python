# The ProcessPoolExecutor class is an Executor subclass that uses a pool of processes to execute calls asynchronously.
# ProcessPoolExecutor uses the multiprocessing module, which allows it to side-step the Global Interpreter Lock
# but also means that only picklable objects can be executed and returned.

import concurrent.futures
import time

start = time.perf_counter()


def do_a_task(seconds) -> str:
    print(f'Sleeping for {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [i for i in range(1, 6)]
    results = executor.map(do_a_task, secs)

    for res in results:
        print(res)

finish = time.perf_counter()

print(f'finished in {round(finish-start, 2)} second(s)...')
