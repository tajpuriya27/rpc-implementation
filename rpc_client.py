import xmlrpc.client
with xmlrpc.client.ServerProxy("https://localhost:8800/") as proxy:
    while(1):
        n = int(input("Enter number to calculate factorial: "))
        print(f"The Factorial of {n} is : {proxy.FactorialFind(n)}")