def longest_word(*args):
    print(args)
    print(type(args))
    leader = ""

    for word in args:
        if type(word) is str:
            if len(word) > len(leader):
                leader = word
    return leader


print(longest_word("Python", "Java", 3, [], "Programming"))


def longest_list(*args):
    print(args)

    leader = []

    for list_ in args:
        if len(list_) > len(leader):
            leader = list_
    return leader


print(longest_list([1, 2], ['a', 'b', 'c'], [3]))
