def palindrome(s):
    return s == s[::-1]

word = "qazaq"
print(palindrome(word))