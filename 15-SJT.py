# Python program to print all permutations 
# using Johnson and Trotter algorithm. 
LEFT_TO_RIGHT = True
RIGHT_TO_LEFT = False
  
# Utility functions for finding the 
# position of largest mobile integer in a[]. 
def searchArr(a, n, mobile): 
    for i in range(n): 
        if a[i] == mobile: 
            return i + 1
  
# To carry out step 1 of the algorithm i.e. 
# to find the largest mobile integer. 
def getMobile(a, dir, n): 
    mobile_prev = 0
    mobile = 0
    for i in range(n): 
        # direction 0 represents RIGHT TO LEFT. 
        if dir[a[i] - 1] == RIGHT_TO_LEFT and i != 0: 
            if a[i] > a[i - 1] and a[i] > mobile_prev: 
                mobile = a[i] 
                mobile_prev = mobile 
        # direction 1 represents LEFT TO RIGHT. 
        if dir[a[i] - 1] == LEFT_TO_RIGHT and i != n - 1: 
            if a[i] > a[i + 1] and a[i] > mobile_prev: 
                mobile = a[i] 
                mobile_prev = mobile 
    if mobile == 0 and mobile_prev == 0: 
        return 0
    else: 
        return mobile 
  
# Prints a single permutation 
def printOnePerm(a, dir, n): 
    mobile = getMobile(a, dir, n) 
    pos = searchArr(a, n, mobile) 
  
    # swapping the elements according to 
    # the direction i.e. dir[] 
    if dir[a[pos - 1] - 1] == RIGHT_TO_LEFT: 
        a[pos - 1], a[pos - 2] = a[pos - 2], a[pos - 1] 
  
    elif dir[a[pos - 1] - 1] == LEFT_TO_RIGHT: 
        a[pos], a[pos - 1] = a[pos - 1], a[pos] 
  
    # changing the directions for elements 
    # greater than largest mobile integer 
    for i in range(n): 
        if a[i] > mobile: 
            if dir[a[i] - 1] == LEFT_TO_RIGHT: 
                dir[a[i] - 1] = RIGHT_TO_LEFT 
            elif dir[a[i] - 1] == RIGHT_TO_LEFT: 
                dir[a[i] - 1] = LEFT_TO_RIGHT 
  
    for i in range(n): 
        print(a[i], end='') 
    print("") 
  
# To end the algorithm for efficiency it ends 
# at the factorial of n because number of 
# permutations possible is just n!. 
def fact(n): 
    res = 1
    for i in range(1, n + 1): 
        res = res * i 
    return res 
  
# This function mainly calls printOnePerm() 
# one by one to print all permutations. 
def printPermutation(n): 
  
    # To store current permutation 
    # storing the elements from 1 to n and 
    a = [i + 1 for i in range(n)] 
  
    # Printing the first permutation 
    for i in range(n): 
        print(a[i], end='') 
    print("") 
  
    # To store current directions 
    # initially all directions are set 
    # to RIGHT TO LEFT i.e. 0. 
    dir = [RIGHT_TO_LEFT for i in range(n)] 
  
    # for generating permutations in the order. 
    for i in range(1, fact(n)): 
        printOnePerm(a, dir, n) 
  
# Driver code 
n = 4
printPermutation(n) 
  
# This Code is Contributed by Prasad Kandekar(prasad264) 
