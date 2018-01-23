def decoration(debug=False):
    def wrap(func):
        def f_wrap(a,b,c):
            if debug:
                print('Function f called with ',a,b,c)
            return print(func(a,b,c))
        return f_wrap
    return wrap

@decoration(debug=True)
def f(a,b,c):
    return a+b+c

f(1,2,3)

@decoration(debug=False)
def f(a,b,c):
    return a+b+c
f(1,2,3)

