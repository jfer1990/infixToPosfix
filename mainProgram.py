from model.Converter import *
from view.terminalView import *





class controller:
    def __init__(self,vista):
        self._vista = vista
        self._evento = self._vista.getVal()
        self.dic = {}
    def iniciar(self):
        self._vista.run(self)


    def control(self,exp):
        if self.isAsignation(exp):
            lista = self.getListExp(exp)
            lista = self.substituteX(lista)
            val = self.evalInfixToPosfix(lista[1])
            self.asignar(lista[0],val)
            print("<< "+lista[0]+"  <-  "+str(self.dic.get(lista[0]))+" >>")
        else:
            lista = self.substituteX(["auxiliar",exp])
            print("<<"+str(self.evalInfixToPosfix(lista[1]))+">>")





#Precondicion: exp sea una lista con 2 elementos, el elemento 0 la variable y el elemento 1 la expresion a evaluar
    def substituteX(self,lista):
        expresion = lista[1]
        for i in range(len(str(expresion))): #para todos los elementos de la expresion
            char=expresion[i]
            if self.isAlpha(char):
                if self.dic.get(char)!=None:
                    aux = str(self.dic.get(char))
                    auxStr = lista[1].replace(char,aux)
                    lista = [lista[0],auxStr]
        return lista

                    #print(expAux)


    def isAsignation(self,exp):
        if len(exp)>2: # x:3 requiere un minimo de 3 caracteres
            if self.isAlpha(exp[0]):
                if str(exp[1]).__eq__(":"):
                    return True
        return False
    #precondicion: recibe un caracter de tipo char
    def isAlpha(self,char):
        if len(char)>1:
            return False
        if (ord(char) >= ord('A') and ord(char) <= ord('Z')) or (
                ord(char) >= ord('a') and ord(char) <= ord('z')):
            return True
        else:
            return False

    #postcondición: retorna 2 elementos en la lista si es una asignación, o devuelve un solo elemento si es una evaluación
    def getListExp(self,exp):
        if self.isAsignation(exp):
            return exp.split(":")
        else:
            return exp.split("\n")
    def asignar(self,var,exp):
        self.dic[var]=exp
    def evalInfixToPosfix(self,exp):
        return evaluatePosfix(infixToPosfix(exp))

vista = mainWindow()
mvc = controller(vista)
mvc.iniciar()