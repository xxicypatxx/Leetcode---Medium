# Sorting Algorithms

## Summary

![summary](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/summary.png)

## 10 Sorting Algorithms with examples

### 1. Bubble Sort

Compare every two elements in the given array.

Repeat until all elements are sorted.

Suitable for small data set.

#### GIF Explanation

![bubble sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/bubble_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**2)```

- Best Case Performance: ```O(n)```

- Worst Case Performance: ```O(n**2)```

- Stable: Yes

#### Code

```python3
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
<br/><br/>


### 2. Selection Sort

Keep searching for the smallest (or biggest) element and swapping it into place.

#### GIF Explanation

![selection sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/selection_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**2)```

- Best Case Performance: ```O(n**2)```

- Worst Case Performance: ```O(n**2)```

- Stable: No

#### Code

```python3
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr
```
<br/><br/>


### 3. Insertion Sort

Suitable for a small number of elements.

#### GIF Explanation

![insertion sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/insertion_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**2)```

- Best Case Performance: ```O(n)```

- Worst Case Performance: ```O(n**2)```

- Stable: Yes

#### Code

```python3
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
```
<br/><br/>


### 4. Merge Sort

Merge Sort is a Divide and Conquer algorithm. 
It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. 
The major portion of the algorithm is given two sorted arrays, and we have to merge them into a single sorted array.

#### GIF Explanation

![merge sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/merge_sort.gif)

![merge sort explanation](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/merge_sort.png)

#### Properties

- Space Complexity: ```O(n)```

- Average Time Complexity : ```O(n*log(n))```

- Best Case Performance: ```O(n*log(n))```

- Worst Case Performance: ```O(n*log(n))```

- Stable: Yes

#### Code

```python3
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
```
<br/><br/>


### 5. Quick Sort

Quick sort is an efficient divide and conquer sorting algorithm.

The steps involved in Quick Sort are:
- Choose an element to serve as a pivot, in this case, the last element of the array is the pivot.
- Partitioning: Sort the array in such a manner that all elements less than the pivot are to the left, and all elements greater than the pivot are to the right.
- Call Quicksort recursively, taking into account the previous pivot to properly subdivide the left and right arrays. 

#### GIF Explanation

![quick sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/quick_sort.gif)

#### Properties

- Space Complexity: ```O(n*log(n))```

- Average Time Complexity : ```O(n*log(n))```

- Best Case Performance: ```O(n*log(n))```

- Worst Case Performance: ```O(n**2)```

- Stable: No

#### Code

```python3
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
```
<br/><br/>


### 6. Heap Sort

Heap is a special **complete binary tree**.
In this way, given an index ```i``` of a node, we can calculate:
- its parent node: ```idx = floor(i / 2)```
- its right child: ```idx = 2 * i```
- its left child: ```idx = 2 * i + 1```

![heap](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/heap.jpg)

There are two kinds of binary heaps:
1. Max Heap - value in a parent node is greater than the values in its two children nodes
2. Min Heap - value in a parent node is smaller than the values in its two children nodes

The steps involved in Heap Sort are:
1. Build Max Heap (or Min Heap);
2. Adjust the heap;
3. Heap Sort.

#### GIF Explanation

![heap sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/heap_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n*log(n))```

- Best Case Performance: ```O(n*log(n))```

- Worst Case Performance: ```O(n**2)```

- Stable: No

#### Code
```python3
import random


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


a = [random.randint(0, 100) for i in range(20)]
heapSort(a)
print(a)
```
<br/><br/>


### 7. Shell Sort

Shell Sort algorithm is an improved version of Insertion Sort algorithm.

#### GIF Explanation

![shell sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/shell_sort.gif)

#### Properties

- Space Complexity: ```O(1)```

- Average Time Complexity : ```O(n**1.3)```

- Best Case Performance: ```O(n)```

- Worst Case Performance: ```O(n**2)```

- Stable: No

#### Code
```python3
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
```
<br/><br/>


### 8. Counting Sort

#### GIF Explanation

![counting sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/counting_sort.gif)

#### Properties

- Space Complexity: ```O(n + k)```

- Average Time Complexity : ```O(n + k)```

- Best Case Performance: ```O(n + k)```

- Worst Case Performance: ```O(n + k)```

- Stable: Yes

(```k``` is the number of distinct elements in the array)

<br/><br/>


### 9. Bucket Sort

Bucket Sort is a comparison sort algorithm that operates on elements by dividing them into different buckets and then sorting these buckets individually. 
Each bucket is sorted individually using a separate sorting algorithm or by applying the bucket sort algorithm recursively.

#### GIF Explanation

![bucket sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/bucket_sort.gif)

#### Properties

- Space Complexity: ```O(n + k)```

- Average Time Complexity : ```O(n + k)```

- Best Case Performance: ```O(n)```

- Worst Case Performance: ```O(n**2)```

- Stable: Yes

#### Code

```python3
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
```
<br/><br/>


### 10. Radix Sort

Do following for each digit i where i varies from least significant digit to the most significant digit:

- Sort input array using counting sort (or any stable sort) according to the i’th digit.

#### GIF Explanation

![radix sort](https://github.com/xxicypatxx/Leetcode---Medium/blob/main/Algorithms/imgaes/radix_sort.gif)

#### Properties

- Space Complexity: ```O(n + k)```

- Average Time Complexity : ```O(n*k)```

- Best Case Performance: ```O(n*k)```

- Worst Case Performance: ```O(n*k)```

- Stable: Yes

#### Code

```python3
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

```
