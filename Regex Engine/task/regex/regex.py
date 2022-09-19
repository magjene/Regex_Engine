"""
Project: Regex Engine
Stage 3/6: Working with strings of different length


Description
At this point, your regex engine is pretty basic and not very useful. Comparing two equal length patterns to each other is not what we usually need. Let's add support for comparing regex-string pairs of different lengths.

For example, the engine will be able to compare the substring tion with the following words and find matches: section, seduction, introduction, intersection, motion, neon, chair, mockingbird. As you can see, this scenario is already more realistic: there is a bunch of words and we only want to select those with a specific suffix.

So, how does it work if our function can only work with regex-string pairs of equal length? Remember, in the previous step we added two terminating conditions to the function: if the regex is consumed, we return True, and if the string is consumed, we return False. The first condition means that we have gone over the whole regex and there is a match. The other case shows that there cannot be a match since the regex has not been consumed and there is no string to compare it to. These two conditions make sure that the function does not break if the text is for some reason longer than the regex or vice versa.

One way to tackle this problem is to repeatedly invoke that function and check if there is a match. If there isn't, another section of the string should be passed.

Let's see how this can be done with our suffix example:

Input: ‘tion|Section’     Output: False
Input: ‘tion|ection’      Output: False
Input: ‘tion|ction’       Output: False
Input: ‘tion|tion’        Output: True
Objectives
Your improved regex engine should do the following:

A new function is created as an entry point;
It should repeatedly invoke the function that compares two equal length patterns;
If that function returns True, the new function should also return True;
If that function returns False, the input string should be passed to the matching function with an incremented starting position, and the regex should be passed unmodified;
The process goes on until the entire input string has been consumed.
A way to implement this is to use slicing like in the previous stages, but do it only to progress the input string.
The input string should be consumed character by character, and the regex should be checked against every position.

A loop can be used to take care of the changing starting characters, but you can also experiment more with recursion.

In case you choose to use a loop, keep in mind that the type of the loop you use is optional, but in order to slice a string, integers should be passed as string indexes, and an index should not be greater than the length of the input string. If the end of the string is reached, the input string is consumed without a match, which should return False.

If you prefer to stick to recursion, use the same logic you used earlier. However, keep in mind that Python has a limit on recursion, and it might be reached if you're dealing with longer strings. To counter this, the following lines should be added to your program if it throws an error message about reaching the recursion limit:

import sys
sys.setrecursionlimit(10000)
Example
Input: 'apple|apple'     Output: True
Input:    'ap|apple'     Output: True
Input:    'le|apple'     Output: True
Input:     'a|apple'     Output: True
Input:     '.|apple'     Output: True
Input: 'apwle|apple'     Output: False
Input: 'peach|apple'     Output: False
"""


# def reg(regex, word):
#     return regex[0] == word[0] or regex[0] == '.'


def match_re_str(regex, word):
    return not regex or word != "" and regex[0] in [word[:1], '.'] and match_re_str(regex[1:], word[1:])


for _ in range(10):
    print(match_re_str(*input().split("|")))
