import xmlrpc.client

# Connect to the server
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("Select arithmetic operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Call appropriate RPC method
if choice == '1':
    result = proxy.add(a, b)
elif choice == '2':
    result = proxy.subtract(a, b)
elif choice == '3':
    result = proxy.multiply(a, b)
elif choice == '4':
    result = proxy.divide(a, b)
else:
    result = "Invalid input"

print("Result:", result)
