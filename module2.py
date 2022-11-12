""""Module 2: Strings, String and List Methods, and Exceptions"""


list = [5,1,6,3,8,4,2,9,0]

print(sorted(list))
print(list)
list.sort()
print(list)


"""Lab Is Palindrome"""
def ispalindrome(s: str):
    if s == s[::-1]:
        print('its a palindrome')
    else:
        print('not a palindrome')\
        
ispalindrome('kayak')
ispalindrome('joey')
