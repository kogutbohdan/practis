array=[0]*100
print(array)
array.extend([3, 6, 7])
print(array)
array[1]=33333
print(array)
array.reverse()
print(array)
array.append(3)
print(array)
i=0
for elem in array:
    if(elem==3):
        del array[i]
    i+=1
print(array)
array.sort()
print(array)
array.clear()
print(array)
