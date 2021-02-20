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