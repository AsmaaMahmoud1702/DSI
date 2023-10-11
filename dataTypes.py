# Number data type: Immutable data types
print("//////// Number Data Type: ////////\n")

num1 = 2 # this is an integer data type
print(f"Integer data type: {num1}, Data type: {type(num1)}\n")

num2 = 2.5 # this is a float data type
print(f"Float data type: {num2}, Data type: {type(num2)}\n")

num3 = 5j # iota (imaginary) data type 
print(f"Iota data type: {num3}, Data type: {type(num3)}\n")

# Sequential data types:
# 1- String data type: Immutable data types
print("//////// String Data Type: ////////\n")

str1 = 'Asmaa'
print(f"String with single quotes: {str1}\nData type: {type(str1)}")
print(f"First two characters (L->R indexing): {str1[0:2]}\n")

str2 = "Mahmoud"
print(f"String with double quotes: {str2}\nData type: {type(str2)}")
print(f"Middle characters (R->L indexing): {str2[-6:-1]}\n") 

str3 ='''Asmaa
Mahmoud'''
print(f"String with triple quotes: {str3}\nData type: {type(str3)}")
print(f"Reverse string: {str3[::-1]}\nString slicing 2 steps: {str3[::2]}\n")
print(f"String concatenation: {str1 + ' ' + str2}")
print(f"String Multiplication: {3 * (str2 + ' ')}\n")

# 2- list data type: Mutable data types
print("//////// List Data Type: ////////\n")
list1 = ["Asmaa", 25 , [12,9], 4.5]
list2 = ["Mahmoud" , 30, [20,30], 10]
print(f"First list: {list1}, Data type: {type(list1)}")
list1.append(100) #Add element to array (Mutable data type) 
print(f"First list: {list1}")
print(f"Value of index 1 in array: {list1[1]}, Multiplying it with 3: {3 * list1[1]}")
print(f"Multiply first list by 2: {2 * list1}\n")

print(f"Second list: {list2}, Data type: {type(list2)}\nList slicing with 2 step: {list2[::2]}")
print(f"Value of index -3 in array: {list2[-3]}, Multiplying it with 3: {3 * list2[-3]}")
print(f"First element in array: {list2[0:1]}, Multiplying it with 3: {3 *( list2[0:1])}")
print(f"Reverse Second list: {list2[::-1]}\n")

print(f"concatenate two lists: {list1 + list2}")


