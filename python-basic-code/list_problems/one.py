# Find the largest/smallest element in a list


data_num1=[22,32,1,45,2,76,34,2,3,8,3]
data_str1=['hello','jaggu','jagadeesh','jaggu']
data_str2=['hello','jaggu']
print(max(data_num1))
print(max(data_str1,key=len))

# Find the second largest number in a list

second_largest=(sorted(set(data_num1)))
print(second_largest[-2])

# Remove duplicates from a list

data_num2=[22,34,1,435,24]
print(set(data_num1))
print(set(data_str1))

# Find common elements between two lists

set_data_num1=set(data_num1)
set_data_num2=set(data_num2)
set_uni=set_data_num1.intersection(set_data_num2)
print(set_uni)

set_data_str1=set(data_str1)
set_data_str2=set(data_str2)
set_str_uni=set_data_str1.intersection(set_data_str2)
print(set_str_uni)

