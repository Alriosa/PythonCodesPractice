
class Car():
    xChasis = 250
    yChasis = 120
    wheels = 4
    on_run = False

    def start(self):
        self.on_run = True

    def status(self):
        if(self.on_run == True):
            print("Is running")
        else:
            print("Is not running")

myCar = Car()


print("The X of the Chasis is ", myCar.xChasis)
print("The Y of the Chasis is ", myCar.yChasis)
myCar.start()
myCar.status()
