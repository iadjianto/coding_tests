# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 17:01:36 2022

@author: isaia

Maximum Beauty

Given an array of integers and an integer k, find the maximum beauty of the array if we break it into k disjoint subarrays.

DEFINE:
    subsum = sum(subarray)
    beauty = sum(i*subsum[i] for i in [1,2,...,k])

    for example, arr = [1, -1, 3, 9, -2, 5] may be broken up into k=4 subarrays:
        [1], [-1], [3,9], [5]

    notice how we omit the term -2. The beauty of this configuration can be given as:
        1*1 + 2*(-1) + 3*(3+9) + 4*5
"""

from itertools import permutations

"""
INPUT: n, k as int
sum_to_n is a helper function to find all possible ways to 
"""
def sum_to_n(n: int,k: int,limit: int = None):
    if k==1:
        yield [n]
        return
    if limit == None:
        limit = n

    start = (n+k-1)//k
    stop = min(limit,n-k+1)+1

    for i in range(start, stop):
        for tail in sum_to_n(n - i, k - 1, i):
            yield [i] + tail

def beauty(array,k):
    beauty = 0
    if len(array) !=k:
        print('array and k do not match')
    else:
        beauty = sum([(i+1)*sum(array[i]) for i in range(k)])
    #print(beauty)
    # print(array)

    return beauty

"""
My solution was to print off a list of differences, and in general find all permutations of spacing out the bins for the subarrays and calculate\
each of the beauty values
"""
arr = [1, -1, 3, 9, -2, 5]
k = 3

def max_beauty(arr: list,k: int):
    n = len(arr)
    perms = []
    max_b = 0

    for i in range(n-k+1):
        for sums in sum_to_n(n-i-1, k):
            for permutation in set(permutations(sums)):
                perms.append(list(permutation))

    for perm in perms:
        for i in range(n-sum(perm)):
            # print(perm)
            idx = i
            #print(idx)
            arrangement = [idx]
            config = []
            for j in range(k):
                idx+=perm[j]
                #print(idx)
                arrangement.append(idx)
            for j in range(k):
                config.append(arr[arrangement[j]:arrangement[j+1]])
            # print(arrangement)
            if max_b < beauty(config,k):
                max_b = beauty(config,k)

    return max_b

for sumi in sum_to_n(10, 4):
    print(sumi)

print(max_beauty(arr, k))