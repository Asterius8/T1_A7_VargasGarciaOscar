'''
Created on 14 mar. 2024

@author: mactec05
'''

class Calculadora:
    
    def __init__(self, primerNumero = 0, operacion="", segundoNumero=0):
        self.primerNumero = float(primerNumero) 
        self.operacion = operacion
        self.segundoNumero = float(segundoNumero)
    
    def sumar(self):
        return float(self.primerNumero) + float(self.segundoNumero)
    
    def resta(self):
        return float(self.primerNumero) - float(self.segundoNumero)
    
    def mult(self):
        return float(self.primerNumero) * float(self.segundoNumero)
    
    def div(self):
        return float(self.primerNumero) / float(self.segundoNumero)
    
    def res(self):
        return float(self.primerNumero)  / 100
    
    def pos_Neg(self):
        
        return float(self.primerNumero) * (-1)
    
    def indicarOperacion_Numero(self, num, op):
        self.primerNumero = num
        self.operacion = op
        print(self.primerNumero)
        print(self.operacion)
        
    def indicarSegundoNumero(self, num):
        self.segundoNumero = num
        print(self.segundoNumero)
        
        
    def realizarOperacion(self):
        
        if(self.operacion=="+"):
            return self.sumar()
        
        elif(self.operacion=="-"):
            return self.resta()
        
        elif(self.operacion=="*"):
            return self.mult()
        
        elif(self.operacion=="/"):
            return self.div()
        
        elif(self.operacion=="%"):
            return self.res()
        elif(self.operacion == "+/-"):
            return self.pos_Neg()

        