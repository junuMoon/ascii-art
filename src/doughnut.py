def draw_rhombus(character, width):
    c = character
    mid = width // 2
    for i in range(mid):
        if not i:
            print("{:>{}}".format(c, mid))
            continue
        print("{:>{}}".format(c, mid-i), end='')
        print("{:>{}}".format(c, i*2))
    for i in range(2, mid):
        print("{:>{}}".format(c, i), end='')
        print("{:>{}}".format(c, width-(i*2)))
    print("{:>{}}".format(c, mid))


if __name__ == '__main__':
    draw_rhombus('@', 10)

