# hard2
def shortPalindrome(s):
    def is_palindrome(string):
        return string == string[::-1]

    n = len(s)

    for i in range(n, 0, -1):
        if is_palindrome(s[:i]):
            return s[i:][::-1] + s

    return s  


s1 = input()  # s = "abcd"
print(shortPalindrome(s1))  # Output: "dcbabcd"