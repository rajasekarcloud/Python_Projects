# Thread pool executor - Demo Without using the thread.
from concurrent.futures import ThreadPoolExecutor;
import time;
values = [3,4,5,6];
t1 = time.perf_counter();
def cube(x):
    for x in values:
        print(f'Cube of {x}:{x*x*x}');
    t2 = time.perf_counter();
    return t2;
if __name__ == '__main__':
    t2 = cube(values);
    print(f'Single Threaded Code Took :{t2 - t1} seconds');

# Code took: Single Threaded Code Took :4.250000000000087e-05 seconds
