# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(len(arr)):
        lower_bound = i # lower bound; 'current' position evaluated
        lowest_ix = lower_bound # assign _lower_ bound of range to the index
                          #     of our current lowest value element
        lowest_x = arr[lower_bound] # assign current lowest value to var 
        # find next smallest element
        for positioninquestion in range(lower_bound, len(arr)):
            if arr[positioninquestion] < lowest_x:
                lowest_x = arr[positioninquestion]
                lowest_ix = positioninquestion
            
        arr[lower_bound], arr[lowest_ix] = arr[lowest_ix], arr[lower_bound]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    # for ix, x in enumerate(arr):
    for x, ix in enumerate(arr):
        swapped = True
        while swapped == True:
            swapped = False
            for ix in range(len(arr) - 1):
            # compare arr[ix] to arr[ix + 1]
            # if curr > next:
                if arr[ix] > arr[ix+1]:
            #   swap
                    arr[ix], arr[ix+1] = arr[ix+1], arr[ix]
            #   increment ix
                    ix += 1
                    swapped = True
            # else:
                else:
            #   increment ix
                    ix += 1
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # check empty case
    if len(arr) == 0:
        return arr

    # initialize an array of 0s of len(maxval+1)        
    if maximum is None:
        maximum = max(arr)
    # initialize 'bins'
    count = [0]*(maximum + 1)

    for ix, x in enumerate(arr):
        if x < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count[x] += 1 # x not ix bc these are bins not indices/positions
    
    # 

    total = 0

    for i in range(maximum+1): # max + 1?
        # count[i], total = total, (count[i] + total)
        temp = count[i] + total
        count[i] = total
        total = temp
    
    output = [0]*len(arr)

    for ix, x in enumerate(arr):
        output[count[ix]] = x
        count[ix] += 1

    return arr
