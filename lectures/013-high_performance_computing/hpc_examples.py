import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process


COUNT = 200000000
SLEEP = 10


def io_bound(sec):

    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(
        f"{pid} * {processName} * {threadName} \
		---> Start sleeping..."
    )
    time.sleep(sec)
    print(
        f"{pid} * {processName} * {threadName} \
		---> Finished sleeping..."
    )


def cpu_bound(n):

    pid = os.getpid()
    threadName = current_thread().name
    processName = current_process().name

    print(
        f"{pid} * {processName} * {threadName} \
		---> Start counting..."
    )

    while n > 0:
        n -= 1

    print(
        f"{pid} * {processName} * {threadName} \
		---> Finished counting..."
    )


def part1():
    # Code snippet for Part 1
    io_bound(SLEEP)
    io_bound(SLEEP)
    io_bound(SLEEP)
    io_bound(SLEEP)
    io_bound(SLEEP)


def part2():
    # Code snippet for Part 2
    t1 = Thread(target=io_bound, args=(SLEEP,))
    t2 = Thread(target=io_bound, args=(SLEEP,))
    t3 = Thread(target=io_bound, args=(SLEEP,))
    t4 = Thread(target=io_bound, args=(SLEEP,))
    t5 = Thread(target=io_bound, args=(SLEEP,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def part3():
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    cpu_bound(COUNT)
    cpu_bound(COUNT)


def part4():
    t1 = Thread(target=cpu_bound, args=(COUNT,))
    t2 = Thread(target=cpu_bound, args=(COUNT,))
    t3 = Thread(target=cpu_bound, args=(COUNT,))
    t4 = Thread(target=cpu_bound, args=(COUNT,))
    t5 = Thread(target=cpu_bound, args=(COUNT,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def part5():
    t1 = Process(target=cpu_bound, args=(COUNT,))
    t2 = Process(target=cpu_bound, args=(COUNT,))
    t3 = Process(target=cpu_bound, args=(COUNT,))
    t4 = Process(target=cpu_bound, args=(COUNT,))
    t5 = Process(target=cpu_bound, args=(COUNT,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


def part6():
    t1 = Process(target=io_bound, args=(SLEEP,))
    t2 = Process(target=io_bound, args=(SLEEP,))
    t3 = Process(target=io_bound, args=(SLEEP,))
    t4 = Process(target=io_bound, args=(SLEEP,))
    t5 = Process(target=io_bound, args=(SLEEP,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()


if __name__ == "__main__":
    start = time.time()

    # part1() # 50 sec
    # part2()  # 10 sec
    # part3() # 164 sec
    # part4()  # 280 sec
    # part5()  # 104 sec
    part6()  # 12 sec

    end = time.time()
    print("Time taken in seconds -", end - start)
