# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5


def length_of_last_word(sentence):
    if len(sentence) == 0:
        return 0

    sentence = sentence.rstrip()

    total_chars = len(sentence)
    i = total_chars - 1
    max = 0;
    while i >= 0:
        if sentence[i] != " ":
            max += 1
        else:
            break
        i -= 1

    return max


print length_of_last_word("a ")
