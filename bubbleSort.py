def bubble_sort(L):
    n = len(L)
    for i in range(0, n):
        for j in range(0, n-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]

if __name__=="__main__":
    L = [6, 1, 4, 9, 2]
    print('before sort: ', L)
    bubble_sort(L)
    print('after sort: ', L)