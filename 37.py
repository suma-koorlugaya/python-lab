Matrix=[[0]*M]*M
sum=0
for i in range(M):
    for j in range(M):
        if i==j:
            sum=sum+Matrix[i][j]
        elif i+j==M-1:
            sum=sum+Matrix[i][j]
print(sum)
