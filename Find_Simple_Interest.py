# Pyhton program for finding Simple Interest.

def simple_interest(p, t, r):
    print("The Simple Principal is ", p)
    print("The time period is ", t)
    print("The rate of interest is ", r)
    si=(p*t*r)/100
    print("The Simple Interest is ", si)
    return si 
    
simple_interest(10, 5, 8)