import Pyro5.api

def main():
    uri = input("Enter server URI: ")  # Copy the URI printed by the server
    checker = Pyro5.api.Proxy(uri)

    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")

    results = checker.check_two_strings(str1, str2)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()
