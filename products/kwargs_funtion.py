def m1(*args, **kwargs):
    print("the type of args is ", type(args))
    print("the type of kwargs is ", type(kwargs))

m1()


def someone(**kwargs):
    for k, v in kwargs.items():
        print(k, ":", v)
someone(name = "jack", age= 20, height= "180cm")