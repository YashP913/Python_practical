import threading
from time import perf_counter
def factorial(n):  # function to calculate factorial


    if (n == 1):
       return n
    return n * factorial(n-1)
def fibonacci(n):  # function to calculate fibonnacci number


    if (n <= 1):
      return n
    return fibonacci(n-1) + fibonacci(n-2)
def cal_fact(n):  # function to print factorial


 print("Factorial of {} is {}.".format(n, factorial(n)))
def fibo_series(n):  # function to print fibonacci series


 print('fibonacci Series:')
 for i in range(n):
  print(fibonacci(i), end=" ")
 print()

time_thread_1 = perf_counter()  # time start
thread_fact = threading.Thread(target=cal_fact, args=[5])
thread_fibo = threading.Thread(target=fibo_series, args=[7])
thread_fact.start()
thread_fibo.start()
thread_fact.join()
thread_fibo.join()
time_thread_2 = perf_counter()  # time end
time_req = time_thread_2 - time_thread_1
print('Time required to perform both operations using multi-threading {}'.format(time_req))
print("Operations completed.")
