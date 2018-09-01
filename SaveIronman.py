import string

T = int(raw_input())


def save_ironman(input_string):
    clean_str = input_string.translate(None, string.punctuation).translate(None, string.whitespace).lower()
    print clean_str
    if clean_str==clean_str[::-1]:
        print ("YES")
    else:
        print ("NO")
    pass


for i in range(0,T,1):
    in_string = raw_input()
    save_ironman(in_string)
