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