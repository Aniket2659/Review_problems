def transpose(matrix):
    transposed=[]
    for i in range(len(matrix[0])):
        temp=[]
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        transposed.append(temp)
    return transposed

matrix=[[1,2,3],[4,5,6]]
print(transpose(matrix))
