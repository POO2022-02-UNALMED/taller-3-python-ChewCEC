class TV:
    numTV = 0

    def __init__ (self, marca, estado):
        self.marca = marca
        self.estado = estado

        self.canal = 1
        self.precio = 100
        self.volumen = 1
        self.numTV =+1 

#marca, control, precio, volumen y canal    

    def setMarca (self,marca):
        self.marca = marca
    
    def getMarca (self):
        return self.marca

    def setControl (self,control):
        self.control = control
    
    def getControl (self):
        return self.control
    
    def setVolumen (self,volumen):
        self.volumen = volumen
    
    def getVolumen (self):
        return self.volumen
    
    def setPrecio (self,precio):
        self.precio = precio
    
    def getPrecio (self):
        return self.precio

    def setCanal (self, canal):
        if (canal>1 and canal<120):
            self.canal = canal
    
    def getCanal (self):
        return self.canal

#turnOn

    def turnOn (self):
        if self.estado == False:
            self.estado = True
     
#turnOff

    def turnOff (self):
        if self.estado == True:
            self.estado = False

#getEstado
    def getEstado (self):
        return self.estado
    
# volumenUp
    def volumenUp (self):
        if (self.getEstado == True and self.getVolumen < 7):
            self.volumen+=1
# volumeDown
    def volumenDown (self):
        if (self.getEstado == True and self.getVolumen > 0):
            self.volumen=-1
# canalnUp

    def canalUp (self):
        if (self.getEstado == True and self.getCanal>1):
            self.canal+=1
            
# canalDown

    def canalDown (self): 
        if (self.getEstado == True and self.getCanal<120):
            self.canal=-1
    
# Set and get numTV

    def setNumTV (self, num):
        self.numTV =  num
    
    def getNumTV (self):
        return self.numTV

