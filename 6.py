from math import floor


def abs(number):
    return -number if number<0 else number


M=int(input())
X=[]

for n in range(-int(19/2),int(19/2)):
    X.append(floor(n))

Y=[]

for n in X:
    if(abs(n)>abs(M)):Y.append(n)

print(M)
print(X)
print(Y)