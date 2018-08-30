# 1
# 360
# 9316 2581 3777 2533 1828 4784 2703 4444 476 8374 2108 7535 4402 3935 4441 1786 393 3320 1414 944 1857 2912 2304 5496 7691 6706 8826 6216 7583 2133 4511 976 2305 9665 3206 9098 2418 7619 6791 5024 467 6850 9934 6495 6975 9075 7694 5787 5465 4762 7639 7508 7460 5682 586 1495 9122 3935 3948 1559 5119 5138 5466 1373 750 2060 9341 2093 8548 406 1918 4268 212 6065 6619 127 8571 3114 8042 7750 2749 1728 1261 9977 8736 4025 1606 465 9783 3953 1405 1626 1153 165 6545 1127 5780 2431 2380 183 1347 723 9081 9063 5544 2249 4426 6440 1662 1291 9029 9698 1598 4978 3727 2825 460 6269 5180 2223 7347 6402 2165 1082 5423 4055 8187 8807 8809 1330 6091 8111 7544 9344 3075 7689 3205 6756 4724 1217 9856 2048 760 2280 1650 2088 4966 1067 5778 1173 3843 9048 5932 1576 763 9598 4335 9616 1857 980 2166 1661 5491 3933 3929 4085 5250 891 4693 3288 6288 786 4057 2559 8827 6910 6226 1290 1241 264 666 74 6692 148 4412 4892 216 158 8827 1159 42 2839 163 1448 6396 6250 2896 3196 9678 9108 3486 3437 5303 323 8001 7041 9845 3630 5094 400 8993 2054 8394 9204 5542 6124 2569 8581 2643 1827 8201 4502 9023 2038 3561 3834 3101 4205 6900 4732 1456 8636 1210 3917 2593 4477 3792 2910 6990 9408 2775 7889 2069 1391 6139 1835 4306 39 2173 1069 7573 1444 1827 4195 3336 395 5102 4316 9007 3022 6764 9948 5008 3772 7008 3790 9157 5047 831 9086 1696 906 7467 1814 6190 5467 5605 5511 2383 4653 1439 4826 1942 1929 7440 3527 8540 3886 8443 9047 2153 8470 610 1605 4709 2971 6471 7242 2332 8842 2420 3225 881 1718 6588 5351 7252 5857 6865 975 7430 1351 6102 5750 1788 6747 72 7290 1219 3717 1993 3760 756 4092 7693 1199 7032 8849 8873 6343 7933 444 856 4486 8025 2364 4000 2332 3022 9145 53 7709 895 6747 4508 9319 1634 7136 3123 6244 8982 2490 3375 6546 439 5048 4565 8962 1168 3719


def createstack():
    stack = []
    return stack


def isempty(stack):
    return len(stack) == 0


def push(stack, x):
    stack.append(x)


def pop(stack):
    if isempty(stack):
        print "Empty Stack"
    else:
        return stack.pop()


def savegotham(a):
    s = createstack()
    ele = 0
    next = 0

    push(s, a[0])
    count = 0
    for i in range(1, len(a), 1):
        next = a[i]

        if not isempty(s):
            ele = pop(s)
            while ele < next:
                count = count + next
                if isempty(s):
                    break
                ele = pop(s)
            if ele >= next:
                push(s, ele)
        push(s, next)

    while not isempty(s):
        ele = pop(s)
        next = 0
        count = count + next
    print count


T = int(raw_input())
for i in xrange(T):
    n = int(raw_input())
    a = map(int, raw_input().rstrip().split())
    savegotham(a)
