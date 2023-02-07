class Athlete:
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def getrunning(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

    def setrunning(self):
        print(self.__name,"won the race in",self.__gender,"'s tornament")

A1 = Athlete("Maria", "girl")
A1.getrunning()
A1.setrunning()

