import Pyro4

uri = input('Enter the server URI: ')
string_concatenator = Pyro4.Proxy(uri)

str1 = input("Enter first string : ")
str2 = input("Enter second string : ")

result = string_concatenator.concatenate(str1, str2)

print('Concatenated String: ', result)