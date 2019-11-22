class Bird:    
    def birdsong(self):
        raise NotImplementedError 

class Chicken(Bird):
    def birdsong(self):
        print('t.t') 

my_chicken = Chicken()
my_chicken.birdsong()