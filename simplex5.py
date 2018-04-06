#   obj_fun Ex: max 3 x1 -4 x2 +5 x3
obj_fun = input('Enter Objective function: ')
obj_list = obj_fun.split()
print(obj_list)

max_min = obj_list[0].lower()

obj_var_list = []
obj_coef_list = []
for i in range(1, len(obj_list), 2):
    obj_coef_list.append(obj_list[i])

for i in range(2, len(obj_list), 2):
    obj_var_list.append(obj_list[i])

obj_dict = {}
for i in range(len(obj_var_list)):
    obj_dict[obj_var_list[i]] = obj_coef_list[i]

print(obj_dict)



####    CONSTRAINT INPUT    ####

constraint_list = []
no_of_constraints = int(input('Enter number of constraints: '))
for i in range(no_of_constraints):
    constraint_list.append(input('Enter constraint %d' %(i+1)))

