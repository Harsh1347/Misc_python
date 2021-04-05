def count(x):

    if x == 0:
        return 0
    print(x)
    return count(x-1)


print(count(10))
