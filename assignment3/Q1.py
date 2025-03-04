# 1. Lambda function to merge two lists into a dictionary
merge_lists = lambda keys, values: {keys[i]: values[i] for i in range(len(keys))}

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = merge_lists(keys, values)
print(result)

