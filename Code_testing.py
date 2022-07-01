def FactorialFind(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact

while(1):
    n = int(input("Enter number to calculate factorial: "))
    print(f"The Factorial of {n} is : {FactorialFind(n)}")