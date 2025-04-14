class TV:
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume = 1  # Range: 0 - 100

    # def power(self):
    #    self.is_on = not self.is_on
    #    state = "ON" if self.is_on else "OFF"
    #    print(f"{self.brand} TV is now {state}.")

    def turnOn(self):
        if self.on == False
            self.on = True
            print("The TV is now turned on.")

    def set_channel(self, channel):
        if self.is_on:
            if 1 <= channel <= 999:
                self.channel = channel
                print(f"Channel set to {self.channel}")
            else:
                print("Invalid channel. Choose between 1 and 999.")
        else:
            print("TV is OFF. Please turn it ON first.")

    def volume_up(self):
        if self.is_on:
            if self.volume < 100:
                self.volume += 1
            print(f"Volume: {self.volume}")
        else:
            print("TV is OFF.")

    def volume_down(self):
        if self.is_on:
            if self.volume > 0:
                self.volume -= 1
            print(f"Volume: {self.volume}")
        else:
            print("TV is OFF.")

    def status(self):
        if self.is_on:
            print(f"TV Status - Brand: {self.brand}, Channel: {self.channel}, Volume: {self.volume}")
        else:
            print("TV is OFF.")

# Example usage
tv = TV("Samsung")
tv.power()
tv.set_channel(5)
tv.volume_up()
tv.volume_down()
tv.status()
tv.power()
