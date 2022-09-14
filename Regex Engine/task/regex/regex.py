"""
Project: Regex Engine
Stage 1/6: Single character strings


Description
In this first stage, create a function that can compare a single character regex to a single character input string.

The reason we are only considering single characters, for now, is the presence of the wild card indicated by a period (.). Its role in a regular expression is to match any character in the target string. So, if the regex that we pass to our function as an argument is a wild-card, the function always returns True no matter what it is being compared to.

When working on this stage, keep in mind the following special rules of the regex syntax:

An empty regex should always return True.
An empty input string should always return False, except if the regex is also empty.
An empty regex against an empty string always returns True.
These rules seem random at first, but later on, they will make sense to you.

Objectives
In this stage, your program should:

Accept two characters, a regex and an input;
Compare the regex to the input and return a boolean indicating if there's a match;
Support . as a wild card character that matches any input;
Follow the special syntax rules outlined above.
We kindly ask you not to use the re module for completing this project. Otherwise, you will learn nothing from it.

Example
Input: 'a|a'     Output: True
Input: '.|a'     Output: True
Input:  '|a'     Output: True
Input:  '|'      Output: True
Input: 'a|'      Output: False
Note that it is purely for technical reasons that the input is a single string divided by the symbol |.

On the left of the delimiter | you will find the regular expression, and on the right is the string that is being compared to that regular expression. The absence of an input character before or after the delimiter indicates that an empty string is passed as an argument. So, if the input is 'a|', you should pass 'a' as a regular expression and '' as an input string to the function.

For valid testing, the results should be printed to the command line. This can be achieved by putting the return value of the function into the print function, which automatically casts the boolean result into a string. You should do this at the end of every stage.

Hint: There are multiple ways to tell if a string is empty. For example, you can use the fact that the length of an empty string is always zero. You may also compare the input string to an empty string literal represented by empty quotation marks ('' or ""). Finally, you can use the boolean logic to determine whether a string is empty.
"""


def reg(r):
    regex, word = r.split("|")
    return regex == word or regex == '.' or regex == ''


l = input()

# while len(l) < 4:
#     print(reg(l))
#     l = input('\nInput reg|str\n')

print(reg(l))

"""
print(reg == str_ or reg == '.' or reg == '')
"""
