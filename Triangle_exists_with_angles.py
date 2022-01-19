# Check if a triangle of positive area is possible with given angles.

def isTriangleExists(a, b, c):
    if(a!=0 and b!=0 and c!=0 and (a+b+c)==180):
        if((a+b)>=c or (b+c)>=a or (a+c)>=b):
            return "yes"
        else:
            return "No"
    else:
        return "No"
a,b,c=50,60,70
print(isTriangleExists(a,b,c))