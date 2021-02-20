# 十大经典排序算法总结

## 1、总体概述

| 排序算法 | 平均时间复杂度 |    最好情况     |    最坏情况     | 空间复杂度  |   排序方式   | 稳定性 |
| :------: | :------------: | :-------------: | :-------------: | :---------: | :----------: | :----: |
| 冒泡排序 |   $O(n^ 2)$    |     $O(n)$      |    $O(n^ 2)$    |   $O(1)$    | $In- place$  |   ✅    |
| 选择排序 |   $O(n^ 2)$    |    $O(n^ 2)$    |    $O(n^ 2)$    |   $O(1)$    | $In- place$  |   ❌    |
| 插入排序 |   $O(n^ 2)$    |     $O(n)$      |    $O(n^ 2)$    |   $O(1)$    | $In- place$  |   ✅    |
| 希尔排序 |  $O(n\log n)$  | $O(n\log ^2 n)$ | $O(n\log ^2 n)$ |   $O(1)$    | $In- place$  |   ❌    |
| 归并排序 |  $O(n\log n)$  |  $O(n\log n)$   |  $O(n\log n)$   |   $O(n)$    | $Out- place$ |   ✅    |
| 快速排序 |  $O(n\log n)$  |  $O(n\log n)$   |    $O(n^ 2)$    | $O(log\ n)$ | $In- place$  |   ❌    |
|  堆排序  |  $O(n\log n)$  |  $O(n\log n)$   |  $O(n\log n)$   |   $O(1)$    | $In- place$  |   ❌    |
| 计数排序 |    $O(n+k)$    |    $O(n+k)$     |    $O(n^ 2)$    |   $O(k)$    | $Out- place$ |   ✅    |
|  桶排序  |    $O(n+k)$    |    $O(n+k)$     |    $O(n^ 2)$    |  $O(n+k)$   | $Out- place$ |   ✅    |
| 基数排序 | $O(n\times k)$ | $O(n\times k)$  | $O(n\times k)$  |  $O(n+k)$   | $Out- place$ |   ✅    |

## 2、分类算法

### 1、冒泡排序

重复走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

![img](https://www.runoob.com/wp-content/uploads/2019/03/bubbleSort.gif)

冒泡排序是最简单的排序方法，其主要思想是在每次循环过滤出数列中最大的数，将其放在最后，因为其比较只在相邻两数之间进行，所以，当大的数初始时越靠前，需要交换的次数就越多，复杂度越大。

优点就是空间复杂度低，且结果稳定。

```python
# bubbleSort.py

from genRand import generateRandom

def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    bubbleSort(arr)
    print(arr)
```

### 2、选择排序

选择排序无论什么数据输入，其时间复杂度都为$O(n^ 2)$，所以输入数据规模越小越好。

![img](https://www.runoob.com/wp-content/uploads/2019/03/selectionSort.gif)

选择排序的主要思想是每次循环选择数列中最小的数据，将其存放到排序序列的前面。

在每次外部循环中，可以设置一个最小索引，用来记录最小数据的索引值，在外部循环结束后，再交换i与最小索引对应的数，可以减少交换次数。

缺点是由于不是逐个交换，在每次外部循环交换时，会打乱大数的次序，所以他的结果是不稳定的。

```python
from genRand import generateRandom

def selectionSort(arr):
    for i in range(len(arr)-1):
        # 记录最小数的索引
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        # i不是最小数时，将i和最小数进行交换
        if i != minIndex:
            arr[i], arr[minIndex] = arr[minIndex], arr[i]
        # print(i, arr)
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    arr = selectionSort(arr)
    print(arr)
```

### 3、插入排序

插入排序在小规模数据或者基本有序时十分高效。

插入排序的过程和打扑克牌整理手牌的原理是一样的，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

![img](https://www.runoob.com/wp-content/uploads/2019/03/insertionSort.gif)

插入排序每次外循环确定一个数的位置，所以在每次内部循环的时候需要一个指针记录已排序数列的位置，将该位置数值与外循环确定的数作比较，若处于之间，将外循环确定数插入到该位置。待每次外循环结束，排序结束。

插入排序优缺点与冒泡排序一样，空间复杂度低，且结果稳定。

```python
from genRand import generateRandom

def insertSort(arr):
    for i in range(len(arr)):
        preIndex = i - 1
        current = arr[i]
        while preIndex>=0 and arr[preIndex]>current:
            arr[preIndex+1] = arr[preIndex]
            preIndex -= 1
        arr[preIndex+1] = current
        # print(i, arr)
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    arr = insertSort(arr)
    print(arr)
```

### 4、希尔排序

希尔排序，是插入排序的一种更高效的改进版本，实现简单，对于中等规模数据的性能表现还不错。

希尔排序基于插入排序提出了两点改进：

1. 插入排序在对几乎已经排序号的数据操作时，效率高，即可以达到线性排序的效率
2. 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位

![img](https://www.runoob.com/wp-content/uploads/2019/03/Sorting_shellsort_anim.gif)

基本思想是：先将整个待排序的记录分割成若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。



```python
from genRand import generateRandom
import math

def shellSort(arr):
    # 初始步长设为总长度的1/k
    k = 2
    gap = len(arr) // k
    while gap >= 1:
        for i in range(len(arr)):
            j = i
            while j>=gap and arr[j-gap]>arr[j]:
                arr[j], arr[j-gap] = arr[j-gap], arr[j]
                j -= gap
        gap = gap // k
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    print(shellSort(arr))
```

### 5、归并排序

归并排序是建立在归并操作上的一种有效的排序算法。

![img](https://www.runoob.com/wp-content/uploads/2019/03/mergeSort.gif)

```python
from genRand import generateRandom

def mergeSort(arr):
    if len(arr)<2:
        return arr
    middle = len(arr) // 2
    left, right = arr[:middle], arr[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0]<=right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    print(mergeSort(arr))
```

### 快速排序

快速排序在平均状况下，排序n个项目要$O(n\ log(n))$次比较，事实上，快速排序通常明显比其他$O(n\ log(n))$算法更快，因为它的内部循环可以在大部分架构和是哪个很有效率地被实现出来。

![img](https://www.runoob.com/wp-content/uploads/2019/03/quickSort.gif)

快速排序是一种分而治之思想在排序算法上的经典应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分支法。

```python
from genRand import generateRandom

def quickSort(arr, left=None, right=None):
    left = 0 if not isinstance(left, (int, float)) else left
    right = len(arr)-1 if not isinstance(right, (int, float)) else right
    if left<right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex-1)
        quickSort(arr, partitionIndex+1, right)
    return arr

def partition(arr, left, right):
    pivot = left
    index = pivot + 1
    i = index
    while i <= right:
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
        i += 1
    arr[pivot], arr[index - 1] = arr[index - 1], arr[pivot]
    return index-1

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    print(quickSort(arr))
```

### 堆排序

堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子节点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。

![img](https://www.runoob.com/wp-content/uploads/2019/03/heapSort.gif)

```python
from genRand import generateRandom

def buildMaxHeap(arr):
    for i in range(len(arr)//2, -1, -1):
        heapify(arr, i)

def heapify(arr, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left<arrLen and arr[left]>arr[largest]:
        largest = left
    if right<arrLen and arr[right]>arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def heapSort(arr):
    global arrLen
    arrLen = len(arr)
    buildMaxHeap(arr)
    for i in range(len(arr)-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arrLen -= 1
        heapify(arr, 0)
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    print(heapSort(arr))
```

### 计数排序

计数排序的核心在于将输入的数值转化为键存储在额外开辟的数组空间中。

![img](https://www.runoob.com/wp-content/uploads/2019/03/countingSort.gif)

```python
from genRand import generateRandom

def countingSort(arr, maxValue):
    bucketLen = maxValue + 1
    bucket = [0]*bucketLen
    sortedIndex = 0
    for i in range(len(arr)):
        if not bucket[arr[i]]:
            bucket[arr[i]] = 0
        bucket[arr[i]] += 1
    for j in range(bucketLen):
        while bucket[j]>0:
            arr[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    print(countingSort(arr, 20))
```

### 桶排序

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。为了使桶排序更加高效，我们需要做到这两点：

1. 在额外空间充足的情况下，尽量增大桶的数量
2. 使用的映射函数能够将输入的N个数据均匀的分配到K个桶中

与计数排序类似，只不过这里是将对应范围的数据放入到桶中排序。

同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响直观重要。

这里代码不再赘述。

### 基数排序

基数排序是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。

基数排序有两种方法：

这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：

- 基数排序：根据键值的每位数字来分配桶；
- 计数排序：每个桶只存储单一键值；
- 桶排序：每个桶存储一定范围的数值；

这里代码不再赘述。

## 附录

最后附上```genRand.python```代码：

```python
# genRand.py
import random

def generateRandom(num):
    arr = []
    for i in range(0, num):
        arr.append(random.randint(0, 20))
    return arr
```

