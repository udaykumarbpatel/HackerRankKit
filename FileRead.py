import sys


def num_of_words_in_file(filename):
    file_obj = open(filename, 'r')

    count = 0
    max_w = -sys.maxint
    max_word = ""
    for line in file_obj:
        words = line.split()
        for w in words:
            if len(w) > 1 and w[0] == w[-1]:
                if len(w) > max_w:
                    max_word = w
                    max_w = len(w)
        if words:
            count += len(words)

    print max_word
    print count


num_of_words_in_file("bubble_sort.py")
