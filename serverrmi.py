import Pyro5.api

@Pyro5.api.expose
class PalindromeChecker:
    def is_palindrome(self, s):
        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    def check_two_strings(self, str1, str2):
        result1 = f'"{str1}" is a palindrome' if self.is_palindrome(str1) else f'"{str1}" is not a palindrome'
        result2 = f'"{str2}" is a palindrome' if self.is_palindrome(str2) else f'"{str2}" is not a palindrome'
        return [result1, result2]

def main():
    daemon = Pyro5.api.Daemon()
    uri = daemon.register(PalindromeChecker)
    print("Server is running. Object URI:")
    print(uri)
    daemon.requestLoop()

if __name__ == "__main__":
    main()
