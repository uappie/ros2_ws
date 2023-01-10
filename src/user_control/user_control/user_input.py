import getch

class UserInput:
 
    def __init__(self):
        self.direction = "c"
        self.speed = 0
        self.speedStep = 85
 
    def changeSpeed(self, speedChange):
        if speedChange == "+":
            self.speed += self.speedStep
            if self.speed > 255:
                self.speed = 255
        elif speedChange == "-":
            self.speed -= self.speedStep
            if self.speed < 0:
                self.speed = 0
 
    def readInput(self):
        print("Command:")
        userInput = getch.getch()#.decode("utf-8")
        if userInput == "+" or userInput == "-":
            self.changeSpeed(userInput)
         
        elif userInput == "w" or userInput == "a" or userInput == "s" or userInput == "d" or userInput == "c":
            self.direction = userInput

        return self.direction + str(self.speed) + "\n"
 
if __name__ == "__main__":
    uc = UserInput()
    while True:
        uc.readInput()
        print(uc.speed)
        print(uc.direction)
     
    