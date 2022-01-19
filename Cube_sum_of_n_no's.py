# Python program for cube sum of first n no's.

def sumofseries(n):
    sum=0
    for i in range (1, n+1):
        sum+=i*i*i
    return sum
n=5
print(sumofseries(n))