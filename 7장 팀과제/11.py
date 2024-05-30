# 11. 0-1 배낭 채우기 알고리즘을 메모이제이션으로 구현해 봐라
def knapSack_memo(W, wt, val, n):
    memo = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
    
    def knapSackRec(w, i):
        if i == 0 or w == 0:
            return 0
        
        if memo[i][w] != -1:
            return memo[i][w]
        
        if wt[i - 1] > w:
            memo[i][w] = knapSackRec(w, i - 1)
        else:
            valWith = val[i - 1] + knapSackRec(w - wt[i - 1], i - 1)
            valWithout = knapSackRec(w, i - 1)
            memo[i][w] = max(valWith, valWithout)
        
        return memo[i][w]
    
    return knapSackRec(W, n)

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)

print(knapSack_memo(W, wt, val, n))