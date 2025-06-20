name="dev Tiwari"
print(len(name))#lenth of a string
print(name.endswith("ari"))
print(name.startswith("De"))
print(name.capitalize())

"""
Python provides a rich set of string methods that allow you to perform various operations on strings. Here are some of the most commonly used string functions in Python:

len(s) - Returns the length of the string s.

s = "hello"
print(len(s))  # Output: 5



s.lower() - Converts all characters in the string s to lowercase.

s = "HELLO"
print(s.lower())  # Output: "hello"



s.upper() - Converts all characters in the string s to uppercase.

s = "hello"
print(s.upper())  # Output: "HELLO"



s.title() - Converts the first character of each word to uppercase and the rest to lowercase.

s = "hello world"
print(s.title())  # Output: "Hello World"



s.capitalize() - Converts the first character to uppercase and the rest to lowercase.

s = "hello world"
print(s.capitalize())  # Output: "Hello world"



s.strip([chars]) - Removes any leading and trailing characters (space is the default) specified in chars.

s = "  hello  "
print(s.strip())  # Output: "hello"



s.lstrip([chars]) - Removes leading characters specified in chars.

s = "  hello  "
print(s.lstrip())  # Output: "hello  "



s.rstrip([chars]) - Removes trailing characters specified in chars.

s = "  hello  "
print(s.rstrip())  # Output: "  hello"



s.split([sep]) - Splits the string into a list of substrings using sep as the delimiter.

s = "a,b,c"
print(s.split(','))  # Output: ['a', 'b', 'c']



s.join(iterable) - Concatenates a list or iterable of strings using s as the separator.

s = "-"
seq = ("a", "b", "c")
print(s.join(seq))  # Output: "a-b-c"



s.find(sub[, start[, end]]) - Returns the lowest index where the substring sub is found in the string; returns -1 if not found ( to find the index number)
s = "hello world"
print(s.find('world'))  # Output: 6



s.replace(old, new[, count]) - Replaces occurrences of substring old with new. If count is specified, only the first count occurrences are replaced.
s = "hello world"
print(s.replace('world', 'there'))  # Output: "hello there"



s.startswith(prefix[, start[, end]]) - Returns True if the string starts with prefix, otherwise False.
s = "hello world"
print(s.startswith('hello'))  # Output: True



s.endswith(suffix[, start[, end]]) - Returns True if the string ends with suffix, otherwise False.
s = "hello world"
print(s.endswith('world'))  # Output: True



s.isdigit() - Returns True if all characters in the string are digits.

s = "12345"
print(s.isdigit())  # Output: True



s.isalpha() - Returns True if all characters in the string are alphabetic.

s = "hello"
print(s.isalpha())  # Output: True



s.isnumeric() - Returns True if all characters in the string are numeric characters.

s = "12345"
print(s.isnumeric())  # Output: True



s.islower() - Returns True if all characters in the string are lowercase.

s = "hello"
print(s.islower())  # Output: True



s.isupper() - Returns True if all characters in the string are uppercase.

s = "HELLO"
print(s.isupper())  # Output: True



These methods provide a wide range of functionalities for string manipulation and analys###
"""