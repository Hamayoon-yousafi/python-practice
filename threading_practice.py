# not using threading module
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} seconds...")
#     time.sleep(seconds)
#     print("Done Sleeping...")

# do_something(5)
# do_something(5)

# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} seconds.")

# the above code would take around 10 seconds to run, because each function call takes 5 seconds of sleep so 5+5=10
# however we can use multithreading module to benefit from concurrency and not wait for the first function call to finish.
# both function calls can run concurrently at the same time without having to wait for the other to finish. So this entire code can run
# about 5 seconds and both function calls run simultaneously and concurrently at the same time taking overall 5 seconds shared.


# above programme but using threading module (older method: without using pools):
# import time 
# import threading

# start = time.perf_counter()

# def do_something(seconds):
#     print(f"Sleeping {seconds} second...")
#     time.sleep(seconds)
#     print("Done Sleeping...")

# thread1 = threading.Thread(target=do_something, args=[5])
# thread2 = threading.Thread(target=do_something, args=[5])
# thread1.start()
# thread2.start()

# the above two lines will start the threads, however the output will be as:
#############################
# Sleeping 5 second...
# Sleeping 5 second...
# Finished in 0.0 seconds.
# Done Sleeping...
# Done Sleeping...
#############################
# the first line in the function and last line which is print() statement will be executed immediately, 
# but the "Done sleeping..."" will be printed after 5 seconds. So the programme only waited 5 seconds for the "Done sleeping..."
# but continued on with the rest of the script concurrently and executed everything else in 0.0 seconds thus printed "Finished in 0.0 seconds".

# to avoid this kind of behavior, we need to call join method which will wait for the sleep time (5 seconds) and continue running the rest of the script
# thread1.join()
# thread2.join()

# output now:
###########################
# Sleeping 5 second...
# Sleeping 5 second...
# Done Sleeping...
# Done Sleeping...
# Finished in 5.0 seconds.
###########################

# finish = time.perf_counter()

# print(f"Finished in {round(finish-start, 2)} seconds.")

# above programme but using concurrent.futures (new method):
import time
import concurrent.futures

start = time.perf_counter()

def do_something(seconds):
    print(f"Sleeping {seconds} seconds...")
    time.sleep(seconds)
    return f"Done Sleeping... after {seconds}"

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something, 5)
    # f2 = executor.submit(do_something, 5)
    # print(f1.result())
    # print(f2.result())

# using map instead of submit: we can create these future objects as above f1 and f2 by simply running a loop, however, the map method makes it easy for us
    args = [2, 4, 5, 1, 3]
    results = executor.map(do_something, args)
    for result in results:
        print(result)

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} seconds.")