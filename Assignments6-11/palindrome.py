def isPalindrome(my_str):
    my_str = my_str.casefold()
    rev_str = reversed(my_str)
    if list(my_str) == list(rev_str):
        print("{} is palindrome".format(my_str))
    else:
        print("{} is not palindrome".format(my_str))