class example:
    def __init__(self,name):
        print(f"First constructor: hello {name}")
        
    def __init__(self,age):
        print(f"Second constructor: Age is {age}")
        
obj=example(28)

class example:
    def __init__(self,*args):
        if len(args)==1:
            print(f"fellow {args[0]}")
        else:
            print(f"Hello {args[0]}, you are {args[1]} old")