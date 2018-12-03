Matrix_1 = [[1,2],[3,3]]
Matrix_2 = [[7,3],[9,4]]
Matrix_3 = []

row = 2
column = 2
i = 0
j = 0
for i in range(len(Matrix_2)):
    for j in range(len(Matrix_2)):
        add = Matrix_1[i][j]+Matrix_2[i][j]
        # Matrix_3 = Matrix_3[:i+j] + [add]
        Matrix_3.append(add)

print(Matrix_3)
