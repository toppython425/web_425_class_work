def printargs(args):
    lng = len(args)
    if lng == 0:
        print('')
    elif lng == 1:
        print(args[0])
    else:
        print(str(args))


try:
    raise Exception
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    printargs(e.args)

try:
    raise Exception("my_exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    printargs(e.args)

try:
    raise Exception("my", "exception")
except Exception as e:
    print(e, e.__str__(), sep=' : ', end=' : ')
    printargs(e.args)
