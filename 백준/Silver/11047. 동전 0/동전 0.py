N, K = map(int, input().split())  
A = []
A = [int(input()) for i in range(N)]

cnt = 0
while K > 0 :
    if K >= A[N - 1] :
        cnt += K // A[N - 1]
        K = K % A[N - 1]
    N -= 1
print(cnt)