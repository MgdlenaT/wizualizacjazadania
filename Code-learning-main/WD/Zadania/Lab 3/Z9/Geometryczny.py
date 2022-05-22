
class Ciag():

    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def n_ty_wyraz(self):
        d = self.a + (self.b-1) * self.c
        print(d)
    
    def suma_pierwszych_wyrazow(self):
        d = self.a + (self.b -1) * self.c
        s = ((self.a + d)/2) * self.b