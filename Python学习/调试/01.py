def SayHello(name):
    print("hi,{0}".format(name))
    print("done....")
    return None

if __name__ == "__main__" :
    print("*"*10)
    name = input("input name:")
    print(SayHello(name= name))
    print("@@"*10)