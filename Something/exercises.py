# ---   reversed string   -----------------------------------------------------------------------------------------------------------
def my_fn(string):
    result_string = ""
    for i in range(len(string) - 1, -1, -1):
        result_string += string[i]
    return result_string


# ---   check same case   -----------------------------------------------------------------------------------------------------------
def my_fn1(a, b):
    if not a.isalpha() or not b.isalpha():
        return -1
    if a.isupper() == b.isupper():
        return 1
    else:
        return 0


# ---   points of reflections   -----------------------------------------------------------------------------------------------------------
def my_fn2(a, b):
    diff_x = a[0] - b[0]
    diff_y = a[1] - b[1]

    x = a[0] + diff_x
    y = a[1] + diff_y

    return [x, y]


