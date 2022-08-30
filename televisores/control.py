
class Control:
    
    def __init__ (self):
        self.TV = None
    
    def getTV (self):
        return self.TV

    def setTV (self, tv):
        self.TV = tv
    
    def enlazar (self,tv):
        self.setTV(tv)
        tv.setControl(self)

    def turnOff (self):
        self.TV.turnOff
    
    def turnOn (self):
        self.TV.turnOff
    
    def volumenUp (self):
        self.TV.volumenUp

    def volumenDown(self):
        self.TV.volumenDown
    
    def canalUp (self):
        self.TV.canalUp
        
    def canalDown (self):
        self.TV.canalDown

    def getCanal (self):
        self.TV.getCanal
    
    def setCanal (self,cambio):
        self.TV.setCanal(cambio)