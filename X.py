#prints X with stars of height n


def plotgrid(x):
    h = x // 2
    default = " " * (h - 1)

    if x % 2 == 1:
        for i in range(x):
            if i == h:
                print(" " * h + "*" + " " * h)
            else:
                if i < h:
                    first = default[:i] + "*" + default[i:]
                else:
                    first = default[i - h - 1:] + "*" + default[:i - h - 1]
                second = first[h::-1]
                print(first + " " + second)
    else:
        for i in range(x):
            if i < h:
                first = default[:i] + "*" + default[i:]
            else:
                first = default[i - h:] + "*" + default[:i - h]
            second = first[h::-1]
            print(first + second)


def plotgrid(x):
    h = x // 2  # convenient halfway point
    default = " " * (h - 1)

    if x % 2 == 1:
        # if odd
        for i in range(x):
            if i == h:
                print(" " * h + "*" + " " * h)
            else:
                if i < h:
                    first = default[:i] + "*" + default[i:]
                else:
                    first = default[i - h - 1:] + "*" + default[:i - h - 1]
                second = first[h::-1]
                print(first + " " + second)
    else:
        # if even
        for i in range(x):
            if i < h:
                first = default[:i] + "*" + default[i:]
            else:
                first = default[i - h:] + "*" + default[:i - h]
            second = first[h::-1]
            print(first + second)


plotgrid(3)
