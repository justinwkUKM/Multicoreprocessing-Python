# Multicoreprocessing Python
The “multi” in multiprocessing refers to the multiple cores in a computer’s central processing unit (CPU). Computers originally had only one CPU core or processor, which is the unit that makes all our mathematical calculations possible. Today, computers typically have anywhere from 2 to 128 cores, meaning that taking advantage of more than one can dramatically improve processing time.

In Python, single-CPU use is caused by the global interpreter lock (GIL), which allows only one thread to carry the Python interpreter at any given time. The GIL was implemented to handle a memory management issue, but as a result, Python is limited to using a single processor. Bypassing the GIL when executing Python code allows the code to run faster because we can now take advantage of multiprocessing. Python’s built-in multiprocessing module allows us to designate certain sections of code to bypass the GIL and send the code to multiple processors for simultaneous execution.

## Traditional programming
The traditional for-loop iteration goes through the list one by one and performs the functions on each item individually. In this model, the loops use only 30 to 40 percent of the available CPU power. If we were to use multiprocessing, the function would be executed on multiple list items at once and up to 100 percent of the CPU could be used on a multicore machine. Best of all, we would see a dramatic reduction in execution time.

## Process VS Pool
The multiprocessing Python module contains two classes capable of handling tasks. The Process class sends each task to a different processor, and the Pool class sends sets of tasks to different processors. 
Pool is most useful for large amounts of processes where each process can execute quickly, while Process is most useful for a small number of processes where each process would take a longer time to execute.

## Process
To use the Process class, place the functions and calculations that are done on each list item in its own function that will take a list item as one of its arguments. Next, import the multiprocessing module, create a new process for each list item, and trigger each process in one call. We keep track of these processes by making a list and adding each process to it. After creating all the processes, take the separate output of each CPU and join them into a single list.

## Pool
To use the Pool class, we also have to create a separate function that takes a list item as an argument like we did when using Process. Then, using the multiprocessing module, create a Pool object called pool. This object has a function called map, which takes the function we want to multiprocess and the list as arguments and then iterates through the list for that function. After calling the function map, close the object to allow for a clean shutdown.

## Summary
Unless you are running a machine with more than 10 processors, the Process code should run faster than the Pool code. Process sends code to a processor as soon as the process is started. Pool sends a code to each available processor and doesn’t send any more until a processor has finished computing the first section of code. Pool does this so that processes don’t have to compete for computing resources, but this makes it slower than Process in cases where each process is lengthy. 

## Caution
The multiprocessed code doesn’t execute in the same order as serial execution. There’s no guarantee that the first process to be created will be the first to start or complete. As a result, multiprocessed code usually executes in a different order each time it is run, even if each result is always the same.
