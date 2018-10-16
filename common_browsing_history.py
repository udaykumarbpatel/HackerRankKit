# We have some clickstream data that we gathered on our client's website. Using cookies, we collected snippets of users' anonymized URL histories while they browsed the site. The histories are in chronological order and no URL was visited more than once per person.

# Write a function that takes two user's browsing histories as input and returns the longest contiguous sequence of URLs that appears in both.

user0 = ["/start.html", "/pink.php", "/register.asp", "/start.html", "/green.html", "/blue.html", "/pink.php",
         "/orange.html", "/red.html"]
user1 = ["/red.html", "/green.html", "/blue.html", "/pink.php", "/register.asp"]
user2 = ["/start.html", "/green.html", "/blue.html", "/pink.php", "/register.asp",
         "/orange.html"]
user3 = ["/blue.html", "/logout.php"]


# f(user0, user2):
#    /pink.php
#    /register.asp
#    /orange.html
# f(user1, user2):
#    /green.html
#    /blue.html
#    /pink.php
#    /register.asp
# f(user0, user3):
#    []
# f(user1, user3):
#    /blue.html


# def find_contiguous_sequence(u1, u2):
#     count = 0
#     res = []
#
#     for x, y in zip(u1, u2):
#         if x == y:
#             count += 1
#             res.append(x)
#         else:
#             return count, res
#
#
# def rotate_list(l, n=1):
#     if n > len(l):
#         n = n // len(l)
#     return l[-n:] + l[:-n]
#
#
# def find(l1, l2):
#     max_cont = 0;
#     max_items = []
#
#     for x in range(len(l1) + 1):
#         l1 = rotate_list(l1)
#         cur_cont, items = find_contiguous_sequence(l1, l2)
#         if cur_cont > max_cont:
#             max_cont = cur_cont
#             max_items = items
#
#     print max_items
#
#
def find_pairs(u1, u2, pos_u1, pos_u2):
    res = []
    len_u1 = len(u1)
    len_u2 = len(u2)
    while pos_u1 < len_u1 and pos_u2 < len_u2:
        if u1[pos_u1] == u2[pos_u2]:
            res.append(u1[pos_u1])
            pos_u1 += 1
            pos_u2 += 1
        else:
            break

    return res


def naive_find_contiguous_sequence(u1, u2):
    res = []
    pos_u1 = 0
    while pos_u1 < len(u1):
        if u1[pos_u1] in u2:
            pos_u2 = u2.index(u1[pos_u1])
            curr_list = find_pairs(u1, u2, pos_u1, pos_u2)
            if len(res) < len(curr_list):
                res = list(curr_list)
        pos_u1 += 1

    return res


print naive_find_contiguous_sequence(user0, user2)
print naive_find_contiguous_sequence(user1, user2)
print naive_find_contiguous_sequence(user0, user3)
print naive_find_contiguous_sequence(user1, user3)
# print find(user0, user2)
