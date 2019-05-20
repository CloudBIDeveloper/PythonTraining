#Add
odd = [1, 9]
odd.insert(1,3)

# Output: [1, 3, 9] 
print(odd)

odd[2:2] = [5, 7,10]

# Output: [1, 3, 5, 7, 9]
print(odd)

#------------------------

my_list = ['p','r','o','b','l','e','m']

# delete one item
del my_list[2]

# Output: ['p', 'r', 'b', 'l', 'e', 'm']     
print(my_list)

# delete multiple items
del my_list[1:5]  

# Output: ['p', 'm']
print(my_list)

# delete entire list
del my_list       

# Error: List not defined
#print(my_list)
