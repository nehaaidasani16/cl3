from xmlrpc.server import SimpleXMLRPCServer

# Define arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Create server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server listening on port 8000...")

# Register functions
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")

# Run server
server.serve_forever()
