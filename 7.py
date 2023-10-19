array=[i for i in range(-100,100)]

print(array)

i=0
for n in array:
    if(n<0):
        array[i]=-n
    i+=1

print(array)