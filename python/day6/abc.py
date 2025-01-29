class dog:
    def sound(self):
        return "bark"
    
class cat:
    def sound(self):
        return "meow"
    
def main():
    d=dog()
    c=cat()
    list1=[]
    list1.append(d.sound())
    list1.append(c.sound())
    for i in list1:
        print (i)
    
main()