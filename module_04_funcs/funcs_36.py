def greet_deeply_curried(greeting):
    def w_separator(separator):
        def w_emphasis(emphasis):
            def w_name(name):
                print(greeting + separator + name + emphasis)

            return w_name

        return w_emphasis

    return w_separator


greet = greet_deeply_curried("Привет")("/.../")("!")
greet("Дмитрий")
greet("Иван")

greet_deeply_curried_lambda = lambda greeting: lambda separator: lambda emphasis: lambda name: print(
    greeting + separator + name + emphasis)

greet_lambda = greet_deeply_curried_lambda("Доброго времени суток")("\\...\\")("?")
greet_lambda("Дмитрий")
greet_lambda("Иван")
