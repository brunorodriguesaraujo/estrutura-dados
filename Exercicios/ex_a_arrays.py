def main():
    num = [0, 1, 2, 3, 4]

    for i in num:
        print("{} x 4".format(i), end=' = ')
        i *= 4
        print(i)


main()
