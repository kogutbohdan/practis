array=[i for i in range(-int(19/2),int(19/2)]

print(array)

i=0
for n in array:
    if(n<0):
        array[i]=-n
    i+=1

print(array)
