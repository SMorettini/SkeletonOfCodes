

class ClassName():
    def __init__(self, a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def do_something(self, a="default_value"):
        return a     

if __name__ == '__main__':

    path=""
    cl = ClassName(a,b,c)
    cl.do_something()
