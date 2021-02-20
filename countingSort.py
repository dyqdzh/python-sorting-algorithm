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
