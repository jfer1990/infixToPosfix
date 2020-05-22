import platform
class mainWindow:
    def __init__(self):
        self._currentSel = None
        self._continue = True
        self._system = platform.system()

    def run(self,controller):
        print("Hi, we are working on "+self._system+" system")
        while self._continue:
            self._currentSel = input(">>").replace(" ","") #se quitan los espacios del input
            if self._currentSel == "quit()":
                self._continue = False
            if not self._continue:
                if self._quit():
                    return True
                continue
            if self._currentSel.casefold() == "h".casefold() or self._currentSel.casefold() == "help".casefold():
                self._help()
                continue
            controller.control(self.getVal())


        return True
    def getVal(self):
        return self._currentSel

    #Métodos privados-----------

    def _help(self):
        print("Welcome to infix to posfix program V1.0 \nin order to leave the program "
              +"write \"quit()\" (of course without quoatations.)")
    def _quit(self):
        resp = input("Sure you want to leave? Y/N:  ")
        if resp.casefold()=="Y".casefold():
            return True
        elif resp.casefold() =="N".casefold():
            self._continue = True
            return False
        else:
            return self.quit()
    def _sendVal(self,vista,controller):
        controller.iniciar(vista)

