class computer:
    def __init__(self,name,price,ram):
        self.name=name
        self.price=price
        self.ram=ram
    def getspecs(self):
        self.name=input("Please provide computer name: ")
        self.price=input("Please provide computer price: ")
        self.ram=input("Please provide computer RAM details: ")
    def displayspecs(self):
        print('computer Name: ',self.name)
        print('computer Price: ',self.price)
        print('computer RAM: ',self.ram)
class desktop(computer):
    def __init__(self,gift):
        self.gift=gift
    def get_desktop(self):
        self.gift=input("Please provide desktop freebies detail: ")
        obj1.getspecs()
    def print_desktop(self):
        print('Friebies with Desktop: ',self.gift)
        obj1.displayspecs()
class laptop(computer):
    def __init__(self,weight):
        self.weight=weight
    def get_laptop(self):
        self.weight=input("Please provide laptop weight: ")
        obj2.getspecs()
    def print_laptop(self):
        print('Laptop Weight: ',self.weight)
        obj2.displayspecs()

print("-----------------------Enter Desktop Details-------------------")        
obj1=desktop('')
obj1.get_desktop()

print("-----------------------Enter Laptop Details-------------------")    
obj2=laptop('')
obj2.get_laptop()

print("-----------------------Desktop Details-------------------")
obj1.print_desktop()
print("-----------------------Laptop Details-------------------")
obj2.print_laptop()
