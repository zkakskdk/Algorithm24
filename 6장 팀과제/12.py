# 12. 알파벳 소문자와 대문자(a~z, A~Z)만으로 이루어진 리스트를 알파벳 순으로 정렬하는 코드를 카운팅 정렬로 구현하라
def counting_sort(A):
    MAX_VAL = 52 

    output = [0] * len(A)
    count = [0] * MAX_VAL

    for i in A:
        if 'a' <= i <= 'z':
            count[ord(i) - ord('a')] += 1
        elif 'A' <= i <= 'Z':
            count[ord(i) - ord('A') + 26] += 1

    for i in range(1, MAX_VAL):
        count[i] += count[i-1]

    output = [''] * len(A)

    for i in range(len(A)-1, -1, -1):
        if 'a' <= A[i] <= 'z':
            output[count[ord(A[i]) - ord('a')] - 1] = A[i]
            count[ord(A[i]) - ord('a')] -= 1
        elif 'A' <= A[i] <= 'Z':
            output[count[ord(A[i]) - ord('A') + 26] - 1] = A[i]
            count[ord(A[i]) - ord('A') + 26] -= 1

    for i in range(len(A)):
        A[i] = output[i]

unsorted_list = ['b', 'A', 'c', 'D', 'a', 'B', 'Z', 'y', 'x', 'C', 'd', 'Y']

counting_sort(unsorted_list)

print("정렬된 리스트:", unsorted_list)