## hackerrank probloem link :
## https://www.hackerrank.com/contests/smart-interviews/challenges/si-spiral-traversal-of-matrix/problem

def print_spiral(N, mat):
    sr = sc = 0
    er = ec = N-1
    
    count = 0
    while count < N*N:
        #1. print sr from L -> R
        for j in range(sc, ec+1):
            print(mat[sr][j], end=' ')
            count += 1
        #2. change sr
        sr += 1
        if count >= N*N:
            break
            
        #3. print ec from T -> B
        for j in range(sr, er+1):
            print(mat[j][ec], end=' ')
            count += 1
        #4. change ec
        ec -= 1
        if count >= N*N:
            break
            
        #5. print er from R -> L
        for j in reversed(range(sc, ec+1)):
            print(mat[er][j], end=' ')
            count += 1
        #6. change er
        er -= 1
        if count >= N*N:
            break
            
        #7. print sc from B -> T
        for j in reversed(range(sr, er+1)):
            print(mat[j][sc], end=' ')
            count+=1
        #8. change sc
        sc += 1
        if count >= N*N:
            break
    print()
        

if __name__ == "__main__":
    T = int(input().strip())
    for ti in range(T):
        N = int(input().strip())
        mat = []
        for ni in range(N):
            rowList = list(map(int, input().strip().split(' ')))
            mat.append(rowList)
            
        print_spiral(N, mat)
