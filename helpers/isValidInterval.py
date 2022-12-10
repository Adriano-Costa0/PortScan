def isValid(expression) -> bool:
    if not (expression):
        return
    args = expression.split("-")
    [start, end] = args

    if len(args) != 2 and not (int(start) and int(end)):
        return False

    return True
