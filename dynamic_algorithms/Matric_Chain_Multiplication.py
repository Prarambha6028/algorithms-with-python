def ChainMul(s):
    n=len(s)
    m=[[0]*n for _ in range(n)]
    y=[[0]*n for _ in range(n)]
    for i in range(1,n):
        m[i][i]=0
    for l in range(2,n):
        for i in range(1,n-l+1):
            j=i+l-1
            m[i][j]=float('inf')
            for k in range(i,j):
                q=m[i][k]+m[k+1][j]+s[i-1]*s[k]*s[j]
                if q<m[i][j]:
                    m[i][j]=q
                    y[i][j]=k
    return m,y,m[1][n-1]



sequence=[4,10,3,12,20,7]
result,res,final_res=ChainMul(sequence)
print("Final Result:",final_res)
for i in range(len(sequence)):
    print(result[i])
print('\n')
for i in range(len(sequence)):
    print(res[i])
