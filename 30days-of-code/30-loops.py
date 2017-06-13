if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n < 2) or (n > 20):
        print("error condition")
        exit(0)

    for i in range(10):
        print "%s x %s = %s " % (str(n), str(i+1), str(n*(i+1)))
