'''
Problem 2
Given an array a of n numbers and a count k find the k largest values in the array a.
Example: a=[5, 1, 3, 6, 8, 2, 4, 7], k=3 ⇒ [6, 8, 7]
'''

def kLargest(arr, k): 
    # Sort the given array arr in reverse order. 
    arr.sort(reverse = True) 
    # Print the first kth largest elements 
    for i in range(k): 
        print (arr[i])  
  
# Driver program 
arr = [5, 1, 3, 6, 8, 2, 4, 7]
# n = len(arr) 
k = 3
kLargest(arr, k) 