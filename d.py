##Get the values of a, b and c (coefficients of ##quadratic equation) as input from the user and ##calculate the
##roots and print as the output.

##Input
##Enter the value of a, b and c: 1 -6 9
##Output
##Roots are equal
##Root 1= root 2 = 3.00


import math
a=int(input('enter a value for a:'))
b=int(input('enter a value for B:'))
c=int(input('enter a value for C:'))
if a==0:
    print('a cannot be zero')
else:
    d = b**2-4*a*c
    root=math.sqrt(abs(d))
    if d>0:
        print("Two real roots")
        print((-b+root)/(2*a))
        print((-b-root)/(2*a))
    elif d==0:
        print('roots are empty')
        print(-b/2(2*a))
    else:
        print('No real root')
        print(-b/(2*a),"i",root)
        print(-b/(2*a),"-i",root)