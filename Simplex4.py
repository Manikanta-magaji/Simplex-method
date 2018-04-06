
obj_list = []
constraint = []
constraint_list = []
delta = []

BV = []
XB = []
CB = []

#   Checks for DELTA values.
def check_delta():
    for i in delta:
        if i < 0:
            return True
    return False


#   ========= program execution starts here ============

no_of_variables = int(input('Enter number of variables in objective function: '))
no_of_constraints = int(input('Enter the number of constraints involved: '))



#   ======= input_objective(no_of_variables, no_of_constraints) =========

obj = input('Enter the objective function co-efficients: ')
for i in range(no_of_variables):
    obj_list.append(int(input('x%d? ' %(i+1) )))

for i in range(no_of_constraints):
    obj_list.append(0)




#   ======= input_constraint(no_of_constraints) =========

print('Enter Co-efficients of the constraint: ')

for i in range(no_of_constraints):
    print('\nEnter constraint', i+1)
    for j in range(no_of_variables + no_of_constraints):
        if j < no_of_variables:
            constraint.append(int(input('x%d? ' %(j+1) )))
        else:
            #   adding identity matrix
            if (no_of_variables + i == j ) :  # insert 1 to corresponding constraint
                constraint.append(1)
            else:
                constraint.append(0)

    constraint_list.append(constraint)
    constraint = []

    XB.append(int(input('RHS ? ')))




#   =======  ========


print('obj function:    ', obj_list, '\n')

print('XB: ')
for i in XB:
    print(i)
print('\n')

print('Constraints: ')
for i in constraint_list:
    print(i)




#   ========= initialize BV & CB column ============

for bv in range(no_of_constraints):
    BV.append(no_of_variables + bv)

for j in range(no_of_constraints):
    CB.append(0)

#   ==========





#   ============ claculate_delta()  ==============

for i in range(no_of_constraints + no_of_variables):
    delta.append(0)



for j in range(no_of_variables + no_of_constraints):
    for i in range(no_of_constraints):
        delta[j] += XB[i] * CB[i]   # summation(CB * XB)
    delta[j] -= obj_list[j]     # Delta = summation(CB * XB) - Cj

print('Delta values:')
for i in range(no_of_constraints + no_of_variables):
    print(delta[i], end='\t')
