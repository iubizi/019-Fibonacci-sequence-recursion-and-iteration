import sys
sys.setrecursionlimit(10000)

import functools
@functools.lru_cache # fast recursion
def fib_recursion(n):
    if n <= 2:
        return 1
    return fib_recursion(n-1) + fib_recursion(n-2)



def fib_iteration(n):
    a = b = 1
    for _ in range(n-1):
         a, b = b, a+b
    return a



if __name__ == '__main__':

    for n in range(20):
        print(fib_recursion(n), end='\t')
        print(fib_iteration(n))
        
'''
1	1
1	1
1	1
2	2
3	3
5	5
8	8
13	13
21	21
34	34
55	55
89	89
144	144
233	233
377	377
610	610
987	987
1597	1597
2584	2584
4181	4181
'''
