
from numpy import true_divide


def check_palindrome(str1):

    st=0
    end=len(str1)-1
    while st<=end:
        if str1[st]!=str1[end]:
            return False

        st=st+1
        end=end-1

    return True

print(check_palindrome("abcdcba"))
print(check_palindrome("abbcba"))