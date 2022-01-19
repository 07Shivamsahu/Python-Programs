# Check if Binary representation is palindrome.

def isPalindrome(n):
    rev = 0
    k = n
    while k > 0:
        rev = (rev << 1) | (k & 1)
        k = k >> 1          
    return n == rev
 
if __name__ == '__main__':
    n = 9
    if isPalindrome(n):
        print(f'{n} is a palindrome')
    else:
        print(f'{n} is not a palindrome')