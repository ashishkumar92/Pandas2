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
