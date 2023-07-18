# Thread pool executor - Demo using the thread.
import concurrent.futures;
import time;
values = [3,4,5,6];
t1 = time.perf_counter();
def cube(x):
    for x in values:
        print(f'Cube of {x}:{x*x*x}');

def thread():
    with concurrent.futures.ThreadPoolExecutor(3) as executor:
        executor.submit(cube,values);
    t2 = time.perf_counter();
    print(f'MultiThreaded Code Took:{t2 - t1} seconds');
    
if __name__ == '__main__':
    thread();

# It took MultiThreaded Code Took:0.0034259999999999985 seconds
