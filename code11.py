class overlod:
    def __init__(self,x):
        self.x=x
        #self.y=y
    def __mul__(self, other):
        x=self.x*other.x
        #y=self.y*other.y
        return overlod(x)
    def __str__(self):
        return '({0})'.format(self.x)

p1=overlod('cat-')
p2=overlod(8)

print(p1*p2)
        
