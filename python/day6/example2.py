class example:
    def __init__(self,name,**args):
        self.name=name
    if "name" in args and "age" in args:
        print(f"hello {args['name']}, you are {args['age']}")
    