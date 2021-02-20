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
