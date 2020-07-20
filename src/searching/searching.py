def linear_search(arr, target):
    # iterate over array
    for ix in range(len(arr)):
    #   check if each element is equivalent to target
        if arr[ix] == target:
    #       if so, return the index of that element
            return ix
    # otherwise, return invalid result
    return -1   # not found



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    lower = 0               # lower bound index
    upper = len(arr) - 1    # upper bound index
    
    # define loop-initiating condition
    while lower <= upper:
        
        # compare target to midpoint
        mid = (upper + lower) // 2
        
        if target < arr[mid]:
            # disregard upper elements
            #   reassign upper to mid - 1
            upper = mid - 1

        elif target > arr[mid]:
            # disregard lower elements
            #   reassign lower to mid + 1
            lower = mid + 1
        
        # if ==, return mid
        else:
            return mid
    
    # reached outside our range
    return -1  # not found
