# For Sullivan 2019 Pycon "FUN CODE" contest


def string_to_bool(my_str):
    return my_str.lower() in ("yes", "true", "t", "1")


def compare_boolean(a, b):
    if str(a) is str(b):
        return True
    return False


if __name__ == '__main__':
    val1 = string_to_bool("True")
    val2 = string_to_bool("False")
    # val2 = string_to_bool("True")

    if compare_boolean(val1, val2):
        print("val1 and val2 are the same")
    else:
        print("val1 and val2 are different")

