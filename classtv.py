class TV:
    def __init__(self):
        self.channel = 1
        self.volume = 1
        self.on = False
    def turnOn(self):
        self.on = True
    def turnOff(self):
        self.on = False
    