# n = 9
# a = [112, 133, 161, 311, 122, 512, 1212, 0, 19212]

def SaveGotham(a):
    total = 0
    i = 0
    while i < n-1:
        if a[i] > a[i+1]:
            total = total + a[i+1]
        i = i+1
        total = total + a[i]


    print total % 1000000001



T = int(raw_input())
for i in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().rstrip().split())
    SaveGotham(a)