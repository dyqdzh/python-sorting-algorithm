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