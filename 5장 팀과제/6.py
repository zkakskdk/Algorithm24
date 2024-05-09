# 6. 다음 리스트를 병합 정렬을 이용해 오름차순으로 정렬하라. 각 단계에서의 배열의 내용을 나타내어라. 7 4 9 6 3 8 7 5
def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    temp = []
    i = left
    j = mid + 1

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp.append(A[i])
            i += 1
        else:
            temp.append(A[j])
            j += 1
    
    while i <= mid:
        temp.append(A[i])
        i += 1
    
    while j <= right:
        temp.append(A[j])
        j += 1
    
    for idx, val in enumerate(temp):
        A[left + idx] = val

A = [7, 4, 9, 6, 3, 8, 7, 5]
merge_sort(A, 0, len(A) - 1)
print("정렬된 리스트:", A)

#리스트를 반으로 나눕니다:
#왼쪽 부분 배열: 7 4 9 6
#오른쪽 부분 배열: 3 8 7 5
#각 부분 배열을 재귀적으로 정렬합니다:
#왼쪽 부분 배열: 4 6 7 9
#오른쪽 부분 배열: 3 5 7 8
#정렬된 부분 배열을 병합합니다:
#병합된 배열: 3 4 5 6 7 7 8 9