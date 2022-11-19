Array_A= [5,7,9,11,13]
print(Array_A)
Array_Length = len(Array_A)
print(Array_Length)
print(sum(Array_A))

Array_A = [7,5,10,14,3,9,7]
Array_B = [9,10,3,4,2,5,7,1]
Array_Length = len(Array_A)
Array_Length = len(Array_B)
print(Array_Length)
print(Array_Length)
Array_A.append(15)
print(Array_A)
print(Array_B)
Value = Array_A.count(7)
print(Value)
Value = Array_B.count(7)
print(Value)
Array_A.insert(9,1)
print(Array_A)
Array_B.insert(9,14)
print(Array_B)
Array_C = [7,5,10,14,3,9,7]
Array_C.extend(Array_B)
print(Array_C)
Value = Array_C.count(7)
print(Value)
Array_C.insert(16,3)
print(Array_C)
for i in Array_C:
 if i == 7:
     Array_C.remove(7)
print(Array_C)

from  random import randint
array = ''
for i in range(4):
    e = str(randint(0,8))
    array = array + e
   
array_c = array
print("ID :" ,array_c)
array_P = ["weranat inwakul"]
Status = ["I already have someone next to me."]
arraylength = len(array_P), len(Status)
array_P.extend(Status)
print(array_P)
print("name length :",arraylength)