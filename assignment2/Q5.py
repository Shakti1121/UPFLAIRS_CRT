# 5. Function modifying a list inside a function
def modify_list(lst):
    lst.append("New Item")

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # Output: [1, 2, 3, 'New Item']