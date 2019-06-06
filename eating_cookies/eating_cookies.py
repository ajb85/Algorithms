#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if n == 0: 
    return 1
  elif n < 0:
    return 0
  cache = [0 for i in range(n+1)] if cache == None else cache
  if cache[n] == 0:
    cache[n] = eating_cookies(n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache) # 3^n

  return cache[n]

print(eating_cookies(100))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


    # 1. Determine how many different ways cookie monster can eat n numbers of cookies, knowing that he can either eat 3, 2, or 1 cookies in a given "cycle"

    
