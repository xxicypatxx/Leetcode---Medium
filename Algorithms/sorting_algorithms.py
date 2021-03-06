import random

''' Bubble Sort'''
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


''' Select Sort'''
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


''' Insertion Sort'''
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


''' Merge Sort'''
def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    ret = []
    mid = int(n/2)
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            ret.append(left[0])
            left.pop(0)
        else:
            ret.append(right[0])
            right.pop(0)
    ret += left
    ret += right
    return ret


''' Quick Sort'''
def quickSort(arr):
    n = len(arr)
    if n < 2:
        return arr
    pivot = arr[0]
    left = [item for item in arr if item < pivot]
    mid = [item for item in arr if item == pivot]
    right = [item for item in arr if item > pivot]
    ret = quickSort(left) + mid + quickSort(right)
    return ret


''' Heap Sort'''
def heapify(arr, n, i):
    max_val = i # initialize the largest value as root
    l = 2 * i + 1   # left child idx
    r = 2 * i + 2   # right child idx

    # See if left child of root exists and is greater than the root
    if l < n and arr[i] < arr[l]:
        max_val = l
    # See if right child of root exists and is greater than the root
    if r < n and arr[max_val] < arr[r]:
        max_val = r

    # swap the root, if needed
    if max_val != i:
        arr[i], arr[max_val] = arr[max_val], arr[i]

        # heapify the root
        heapify(arr, n, max_val)



def heapSort(arr):
    n = len(arr)

    # build a max-heap
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    # swap elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


# a = [random.randint(0, 100) for i in range(20)]
# heapSort(a)
# print(a)

''' Shell Sort'''
def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)    # start with a big gap

    while gap > 0:
        for i in range(gap, n):
            key = arr[i]
            j = i
            while j >= gap and arr[j-gap] > key:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = key
        gap = int(gap / 2)


''' Bucket Sort'''
def bucketSort(arr):
    n = len(arr)
    min_val = min(arr)
    max_val = max(arr)

    # calculate the size of the bucket
    bucket_range = (max_val - min_val) / n
    count_list = [[] for i in range(n + 1)]

    # loop the array and put items into each bucket
    for item in arr:
        count_list[int((item - min_val)//bucket_range)].append(item)
    # clear the array
    arr.clear()
    # put items in the bucket back to the array
    for bucket in count_list:
        for item in sorted(bucket):
            arr.append(item)


''' Radix Sort'''
def radixSort(arr):
    n = len(arr)
    max_number_len = len(str(max(arr)))
    # max_number_len rounds of sorting
    for i in range(max_number_len):
        # create a bucket from 0 to 9
        bucket_list = [[] for _ in range(10)]
        for item in arr:
            bucket_list[item//(10**i) % 10].append(item)
        # put items back to the array
        arr = [item for bucket in bucket_list for item in bucket]
    return arr


a = [random.randint(0, 100) for i in range(20)]
print(a)
shellSort(a)
print(a)
