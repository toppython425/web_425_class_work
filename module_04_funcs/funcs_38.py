a = 3
print(f"Global a = {a}")


def get_variable():
    a = 4
    print(f"Local a = {a}")


get_variable()

print(f"Global a = {a}")
