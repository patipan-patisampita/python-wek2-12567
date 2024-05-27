num_string = '12'
num_integer = 23

print('Data type casting:',type(num_string))
#explicit type conversion
num_string = int(num_string)
print(f'Data Type Casting: {num_string}',type(num_string))

num_sum = num_integer + num_string
print(f'Sum: {num_sum}',type(num_sum))
