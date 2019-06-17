def decorate1(func):
    def inner():
      print("before decoration")
      func()
      print("after decoration")
    return inner
def decorate2(func):
    def inner():
        print("decorate-2")
        func()
    return inner


@decorate1
@decorate2

def hello():
    print("hello")

hello()
