# def add(*args):
#     print(sum(args))
#
# add(1,2,3,6,8)

def add(*args):
    for name in args:
        print("I love ", name)

add("小王", "laoliu", "xiaoxia" )