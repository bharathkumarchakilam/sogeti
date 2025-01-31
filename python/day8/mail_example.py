from abc import ABC, abstractmethod

class mail(ABC):
    
    @abstractmethod
    def send(self):
        pass
    
class email(mail):
    
    def send(self):
        print("Hi, I hope your are fine")
        print("sent a message via email")
        print()
        
class sms(mail):
    
    def send(self):
        print("Hi, I hope your are fine")
        print("sent a message via sms")
        print()
         
class whatsapp(mail):
    
    def send(self):
        print("Hi, I hope your are fine")
        print("sent a message via whatsapp")
        print()
        
        
Email=email()
SMS=sms()
Whatsapp=whatsapp()

Email.send()
SMS.send()
Whatsapp.send()
