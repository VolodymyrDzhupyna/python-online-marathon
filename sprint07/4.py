class WashingMachine:

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def startWashing(self):
        self.washing.wash()
        self.rinsing.rins()
        self.spinning.spin()


class Washing:
    
    def wash(self):
        print("Washing...")


class Rinsing:
    
    def rins(self):
        print("Rinsing...")


class Spinning:
    
    def spin(self):
        print("Spinning...")


washingMachine = WashingMachine()
washingMachine.startWashing()
