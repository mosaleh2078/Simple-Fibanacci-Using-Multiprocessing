import os
import random
from multiprocessing import Process

def fibonacci(num:int) -> None:
    result = [0 for _ in range(num + 1)]
    result[1] = 1
    for i in range(2, num + 1):
        result[i] = result[i - 1] + result[i - 2]
    else:
        print(f"Child process {os.getpid()} of parent {os.getppid()} finished with result of fibonacci of {num} = {result[-1]}")

def main(child_num) -> None:
    print(f"Parent process started {os.getpid()}")
    processes = []
    for _ in range(child_num):
        processes.append(Process(target=fibonacci, args=(random.randint(5, 100),)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print("Calculations has been finished")

if __name__ == "__main__":
    child_num = 5
    main(child_num)