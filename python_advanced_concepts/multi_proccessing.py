'''
| Aspect                | Thread                                                                          | Process                                                                   |
| --------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Memory**            | Shared — all threads in one process see the same objects                        | Separate — each process has its own memory (heap)                         |
| **GIL**               | All threads share one GIL — no true CPU parallelism for pure Python code        | Each process has its own GIL — true CPU parallelism                       |
| **Creation Cost**     | ~1 ms — lightweight and cheap                                                   | ~30 ms or more — starts/forks a Python interpreter                        |
| **Communication**     | Shared objects, usually synchronized with `Lock`, `RLock`, `Semaphore`, `Queue` | `Queue`, `Pipe`, `Manager`, Shared Memory                                 |
| **Best For**          | I/O-bound tasks: network requests, file I/O, database queries                   | CPU-bound tasks: image processing, ML, data parsing, scientific computing |
| **Crash Isolation**   | A crashed thread can potentially bring down or corrupt the entire process       | A worker process can crash while the main process continues running       |
| **Context Switching** | Faster (same process memory space)                                              | Slower (separate memory spaces)                                           |
| **Data Sharing**      | Easy (all threads access the same variables)                                    | Harder (data must be copied or explicitly shared)                         |
| **Resource Usage**    | Lower memory usage                                                              | Higher memory usage                                                       |
| **Example Module**    | `threading`                                                                     | `multiprocessing`                                                         |


useful for cpu-bond work 
each proccess has its own memory and own sep gil

'''

import multiprocessing as mp, time
def prime_factors(n):
    factors = []
    d = 2
    c=0

    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            if d==2 or d==5:
                c=c+1
                
            n //= d
        d += 1

    if n > 1:
        factors.append(n)
        if n==2 or n==5:
                c=c+1

    return factors,c

numbers = list(range(1, 50))
# Sequential  
print(prime_factors(2))
t0 = time.time()
# seq = [prime_factors(n) for n in numbers]
# print(seq)
print(f"Sequential: {time.time()-t0:.3f}s")


# Parallel — Pool uses all CPU cores
t0 = time.time()
with mp.Pool(processes=mp.cpu_count()) as pool:
    # par = pool.map(prime_factors, numbers) # blocking; results in input order
# print(f"Parallel ({mp.cpu_count()} cores): {time.time()-t0:.3f}s") # ~4x faster
    pass