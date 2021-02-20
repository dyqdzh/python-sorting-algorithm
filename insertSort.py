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
