import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(pattern='[^\w\s]', repl='', string=s)  # Remove punctuation except underscore
        s = s.lower()  # Convert to lowercase
        s = s.replace(" ", "")  # Remove spaces
        s = s.replace('_', "")
        temp = s[::-1]

        if s == temp:
            return True
        else:
            return False


        

        