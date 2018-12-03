Matrix_1 = [[]]
Matrix_2 = [[]]
Matrix_3 = [[]]
# print(len(Matrix_1))
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

for i in range(row):
    Matrix_1.append(int(input()))
print(Matrix_1)
print(Matrix_2)

for i in range(row):
    for j in range(column):
        add = Matrix_1[i][j]+Matrix_2[i][j]
        Matrix_3 = Matrix_3[:i+j] + [add]
print(Matrix_3)
