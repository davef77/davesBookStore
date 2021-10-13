from _pytest.outcomes import fail


def mandatory(args, tag):
    for arg in args:
        if tag in arg:
            return arg[len(tag) + 2:len(arg)]
    fail("Mandatory parameter " + tag + " not found!")


def optional(args, tag, default_value):
    for arg in args:
        if tag in arg:
            return arg[len(tag) + 2:len(arg)]

    return default_value


