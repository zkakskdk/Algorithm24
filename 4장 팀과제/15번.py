def ternary_search(A, k):
    n = len(A)
    n_1 = n // 3
    n_2 = n_1 * 2
    
    if n == 0:
        return None
    
    if A[n_1] == k:
        return A[n_1]
    elif A[n_2] == k:
        return A[n_2]
    elif A[n_1] > k:
        return ternary_search(A[:n_1], k)
    elif A[n_2] < k:
        return ternary_search(A[n_2 + 1:], k)
    else:
        return ternary_search(A[n_1 + 1:n_2], k)

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = int(input("탐색할 수 입력(1~9) >>"))
print(ternary_search(A, K))