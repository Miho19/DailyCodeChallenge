def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(a , b):
    return a

def cdr(a, b):
    return b

# https://stackoverflow.com/questions/52481607/dont-understand-the-inner-function-in-python