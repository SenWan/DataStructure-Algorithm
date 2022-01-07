def linear_search(L, X):
    n = len(L)
    for i in range(n):
        if L[i] == X:
            return  i

    return -1

if __name__=="__main__":
    A = linear_search([2, 4, 6, 8, 10], 10)
    print(A)