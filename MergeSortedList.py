def merge_sorted_list(l1,l2):
    new_list = []
    len_a = len(l1)
    len_b = len(l2)
    i = j = 0
    while i < len_a and j < len_b:
        if l1[i] < l2[j]:
            new_list.append(l1[i])
            i+=1
        else:
            new_list.append(l2[j])
            j +=1

    while i < len_a:
        new_list.append(l1[i])
        i += 1
    while j < len_b:
        new_list.append(l2[j])
        j +=1

    return new_list


print merge_sorted_list([1,2,4], [1,3,4])