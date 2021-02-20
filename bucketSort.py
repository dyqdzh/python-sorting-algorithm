from genRand import generateRandom

def bucketSort(arr, maxNum):
    buf = {i: [] for i in range(maxNum+1)}
    for i in range(len(arr)):
        num = arr[i]
        buf[num].append(num)
    arr = []
    for i in range(len(buf)):
        if buf[i]:
            arr.extend(sorted(buf[i]))
    return arr

if __name__ == "__main__":
    arr = generateRandom(15)
    print(arr)
    print(bucketSort(arr, 20))