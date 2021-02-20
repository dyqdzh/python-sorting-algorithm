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

