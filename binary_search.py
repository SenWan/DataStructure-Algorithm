def binary_search(L, X):
    left = 0
    right = len(L)-1

    while left <= right:
        mid = (left + right) // 2
        if L[mid] == X:
            return mid

        if L[mid] < X:
            left = mid + 1
        else:
            right = mid - 1

    return  -1

if __name__=="__main__":
    L = [12, 24, 32, 39, 45, 50, 54]
    X = 20

    result = binary_search(L, X)

    if result != -1:
        print("Element is present at index", str(result))
    else:
        print("Element is not present in list1")