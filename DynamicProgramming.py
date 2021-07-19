# Lesson learnt from Dynamic Programming

from time import perf_counter

# Timing the execution time
# This function for decorator. Using @timer before any function
def timer(fn):
    def inner(*args, **kwargs):
        start_time = perf_counter()
        to_execute = fn(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        print('{0} took {1:.4f}s to execute'.format(fn.__name__, execution_time))
        return to_execute
    return

def timing(fn, n):
    start_time = perf_counter()
    result = fn(n)
    end_time = perf_counter()
    execution_time = end_time - start_time
    # print('Fibonaci {} is {} - {} took {3:.4f}s to execute'.format(n, result, fn.__name__, execution_time))
    print('Fibonaci[{0}] is {1} using {2} took {3:.4f} seconds'.format(n, result, fn.__name__, execution_time))


# =====================================================
# ============== Fibonaci Problem =====================
# =====================================================
def Fibonaci_TopDown(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonaci_TopDown(n-1) + Fibonaci_TopDown(n-2)

def Fibonaci_TopDown_Improving(n):
    caching = [-1] * (n+1)
    caching[0] = 0
    caching[1] = 1
    return Fibonaci_TopDown_With_Cache(n, caching)

def Fibonaci_TopDown_With_Cache(n, caching):
    if caching[n] >= 0:
        return caching[n]
    else:
        caching[n] = Fibonaci_TopDown_With_Cache(n-1, caching) + Fibonaci_TopDown_With_Cache(n-2, caching)
        return caching[n]

def Fibonaci_BottomUp(n):
    a, b = 0, 1
    i = 2
    while i <= n:
        a, b = b, a + b
        i += 1
    return b


# =======================================================
# ============== Coin Change Problem ====================
# =======================================================

# Given an integer representing a given amount of change, write a
# function to compute the total number of coins required to make
# that amount of change. You can assume that there is always a
# 1¢ coin.

def CoinChange_TopDown():
    pass

if __name__ == "__main__":
    timing(Fibonaci_TopDown,30)
    timing(Fibonaci_TopDown_Improving, 100)
    timing(Fibonaci_BottomUp, 100)