x = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10']
s = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10']
BV = {}

table = {}

no_of_variables = int(input('Enter number of variables in objective function: '))
no_of_constraints = int(input('Enter the number of constraints involved: '))

for i in range(no_of_constraints):
    table[s[i]] = {}
    for j in range(no_of_variables):
        table[s[i]][x[j]] = int(input())

for i in range(no_of_constraints):
    for j in range(no_of_variables):
        print(table[s[i]][x[j]], end='\t')
    print()