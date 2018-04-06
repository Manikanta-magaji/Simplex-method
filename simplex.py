objective_coef_list = []
constraint = []
constraint_list = []
constraint_RHS = []

#   inputting number of variables and constraints
no_of_variables = int(input('Enter number of variables in objective function: '))
no_of_constraints = int(input('Enter the number of constraints involved: '))


#   inputting objective function values
print('Enter the objective function:')
for i in range(1, no_of_variables + 1):
    objective_coef_list.append(int(input('Enter co efficient of x%d: ' %i)))

max_min = input('Is the objective function maximization or minimization type (max/min)?').lower()

for i in range(1,no_of_constraints + 1):
    print('\nEnter constraint %d' %i)
    for j in range(1, no_of_variables + 1):
        constraint.append(int(input('Enter co efficient of x%d: ' %j)))

    constraint_RHS.append(int(input('It is <= ?')))
    constraint_list.append(constraint)
    constraint = []

print('LPP Model: ')
print(max_min, 'Z = ', end=' ')
for i in range(0, no_of_variables + 1):
    if(objective_coef_list[i+1] < 0):
        print(objective_coef_list[i+1], 'x%d' %(i+1))
    else:
        print('+', objective_coef_list[i+1], 'x%d' %(i+1))

print('Subject to')

for i in range(0, len(constraint_list)):
    for j in range(0, len(no_of_variables)):
        if(constraint_list[i][j] < 0):
            print('%dx%d')

#if max_min == min:



