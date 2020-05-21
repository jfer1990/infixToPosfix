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
        L = self.getListExp(exp)
        self.dic[L[0]] = evaluatePosfix(infixToPosfix(L[1]))
        print(self.dic.get(L[0]))



    def isXvariable(self,exp):
        if (ord(exp[0])>=ord('A') and ord(exp[0])<=ord('Z')) or (ord(exp[0])>=ord('a') and ord(exp[0])<=ord('z')):
            if str(exp[1]).__eq__(":"):
                return True
        return False


    def getListExp(self,exp):
        if self.isXvariable(exp):
            return exp.split(":")
        else:
            return False

vista = mainWindow()
mvc = controller(vista)
mvc.iniciar()