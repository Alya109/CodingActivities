class TV:
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume = 1
        

    def turnOn(self):
        if self.on == False:
            self.on = True
            print("The TV is now turned on.")
        else:
            print("The TV is already turned on.")

    def turnOff(self):
        if self.on == True:
            self.on = False
            print("The TV is now turned off.")
        else:
            print("The TV is already turned off.")

    def getChannel(self):
        if self.on == True:
            return self.channel
        else:
            print("Please turn on the TV first.")
    
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
        else:
            print("Please turn on the TV first.")

    def getVolume(self):
        if self.on == True:
            return self.volume
        else:
            print("Please turn on the TV first.")
    
    def setVolume(self, volume):
        if self.on and 1 <= volume <= 7:
            self.volume = volume
        else:
            print("Please turn on the TV first.")

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1
        else:
            print("Please turn on the TV first.")

    def channelDown(self):
        if self.on and self.channel > 1:
            self.channel -= 1
        else:
            print("Please turn on the TV first.")

    def volumeUp(self):
        if self.on and self.volume < 7:
            self.volume += 1
        else:
            print("Please turn on the TV first.")

    def volumeDown(self):
        if self.on and self.volume > 1:
            self.volume -= 1
        else:
            print("Please turn on the TV first.")

    
