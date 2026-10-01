"""
ASCII (American Standard Code for Information Interchange) is a character
encoding standard that assigns unique numbers from 0 to 127 to English letters,
digits, punctuation marks, and control codes
"""

#Converting Characters to ASCII Values
"""
In Python, you can use the built-in ord() function to convert a single character to its ASCII value.
"""

char = "A"
ascii_value = ord(char)
print(f"The ASCII value of {char} is {ascii_value}")

#--------------------------------------------------------------------
#Converting ASCII Values to Characters
"""
To convert an ASCII value back to a character, you can use the chr() function.
"""
ascii_num = 65
char = chr(ascii_num)
print(f"The character corresponding to ASCII value {ascii_num} is {char}")

#--------------------------------------------------------------------
#Working with ASCII Strings
"""
you can iterate over each character and perform operations on its ASCII value. 
For example, let's convert all lowercase characters in a string to uppercase 
by changing their ASCII values.
"""
string = "hello python"
new_string = ""
for char in string:
    if 97 <= ord(char) <= 122:
        new_char = chr(ord(char) - 32)
        new_string += new_char
    else:
        new_string += char
print(new_string)


#--------------------------------------------------------------------

#Filtering ASCII Characters in a String
import re

def filter_ascii(string):
    return re.sub(r'[^\x00-\x7F]+', '', string)

text = 'Hello, বাংলা!'
filtered_text = filter_ascii(text)
print(filtered_text)

"""
In this code, we use the re module (regular expressions). 
The pattern [^\x00-\x7F] matches any character that is not in 
the ASCII range (0 to 127 in hexadecimal \x00 to \x7F). The re.sub() function 
then replaces all such non-ASCII characters with an empty string.
"""


#--------------------------------------------------------------------
#Validating ASCII-only Input

def is_ascii(in_str):
    return all(ord(char) < 128 for char in in_str)  #The all() function returns True if all items in an iterable are true, otherwise it returns False.

user_input = input("Enter some text: ")
if is_ascii(user_input):
    print("Input contains only ASCII characters.")
else:
    print("Input contains non-ASCII characters.")


#--------------------------------------------------------------------
#Performance Considerations

"""
When working with large strings or performing repeated ASCII-related operations, 
performance can be a concern. Using built-in functions like ord() and chr() is generally fast. 
However, if you need to perform complex operations on a large number of characters, consider using 
more optimized data structures or algorithms. For example, 
if you need to count the occurrences of each ASCII character in a very large string, using a collections.
Counter object can be more efficient.
"""

from collections import Counter

string = 'a' * 1000000
char_count = Counter(string)
print(char_count)