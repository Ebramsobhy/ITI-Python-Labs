# Write a program that generate a multiplication table from 1 to the number passed.

  
def multiplication_table(n):
    table = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(i*j)
        table.append(row)
    return table

n = int(input("Enter the number for multiplication table: "))
table = multiplication_table(n)
for row in table:
    print(row)