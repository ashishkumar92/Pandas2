rowX = int(input("Enter Number of Rows :"))
colX = int(input("Enter Number of Columns :"))
X = []
for i in range(rowX):
    inner_list = []
    for j in range(colX):
        inner_list.append(int(input(f"Enter the value for {i} row and {j} column :")))
    X.append(inner_list)
for i in X:
    print(i)
rowY = rowX
colY = colX
Y = []
for i in range(rowY):
    inner_list = []
    for j in range(colY):
        inner_list.append(int(input(f"Enter the value for {i} row and {j} column :")))
    X.append(inner_list)
for i in Y:
    print(i)
Z = []
rowZ = rowX
colZ = colX
for i in range(rowZ):
    inner_list = []
    for j in range(colZ):
        inner_list.append(X[i][j] + Y[i][j])
    Z.append(inner_list)
for i in Z:
    print(i)