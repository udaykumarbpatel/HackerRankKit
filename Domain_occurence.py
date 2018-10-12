inp_list = ["900,test.google.com", "700,com", "200,test.org"]


def find_occurence(inp_list):
    res = {}
    for i in inp_list:
        val, domain = i.split(',')
        org = domain.split('.')

        for i in org:
            if i in res:
                res[i] = int(res.get(i)) + int(val)
            else:
                res[i] = val

    return res


print find_occurence(inp_list)
