'''
Problem 1
Given an array a of n numbers and a target value t, find two numbers whose sum is t.
Example: a=[5, 3, 6, 8, 2, 4, 7], t=10 ⇒ [3, 7] or [6, 4] or [8, 2]
'''

# input: array(a) of numbers(n), target value(t)
# output: array of two numbers
# no duplicates. positive + negative. all int

# sort first
# have two pointers. one in the beginning, one at the end.
# until two pinters meet each other
# sum up two pointers, check if euqal to target.
# if equal: append to output with array [two pointers]
# if not equal: compare the sum to the target, if the sum is less than the target, move the first pointer to the right, repeat process of finding pair
#                                               if the sum is more than the target, move the last pointer the the left, repeat process.

def findPair(a, target):
    sorted_a = sorted(a)
    # [2, 3, 4, 5, 6, 7, 8]
# first pinter = 2
# last_pointer = 
# total = 9
# output = [[2,8]]

    first_pointer = 0
    last_pointer = len(a) - 1
    output = []

    
    while first_pointer < last_pointer:
        # print(first_pointer)
        print(sorted_a[first_pointer])
        # print(last_pointer)
        print(sorted_a[last_pointer])
        print(output)

        total = sorted_a[first_pointer] + sorted_a[last_pointer]
        if total == target:
            output.append([sorted_a[first_pointer], sorted_a[last_pointer]])
            first_pointer += 1
            last_pointer -= 1
        
        else:

            if total < target:
                first_pointer += 1
            else:
                last_pointer -= 1


    return output

print(findPair([5, 3, 6, 8, 2, 4, 7], 10))