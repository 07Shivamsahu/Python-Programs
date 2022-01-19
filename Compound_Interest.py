# Python program for finding Compound Interest.

def compound_interest(p, r, t):
    print("The principal is ", p)
    print("The rate of interest is ", r)
    print("The time period is ", t)
    Amount=p*(pow((1+r/1000),t))
    CI=Amount-p
    print("Compound Interest is ",CI)
compound_interest(10000, 10.25, 5)