from xmlrpc.server import SimpleXMLRPCServer

#defining function on server side
def FactorialFind(n):
    fact = 1
    if n == 0 or n == 1:
        return fact
    else:
        for i in range(1,n+1):
            fact = fact * i
        return fact

server = SimpleXMLRPCServer(("localhost",8800))
print("listening on port 8800")
server.register_function(FactorialFind, "FactorialFind")
server.serve_forever()

