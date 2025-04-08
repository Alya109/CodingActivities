from classtv import TV

# Making 2 object
tv1 = TV()
tv2 = TV()

# Turning on the TV
tv1.turnOn()
tv2.turnOn()

# Setting the channel and volume for tv1
tv1.setChannel(30)
tv1.setVolume(3)

# Setting the channel and volume for tv2
tv2.setChannel(3)
tv2.setVolume(2)

# Checking status
print(f"tv1's channel is {tv1.getChannel()} and volume level is {tv1.getVolume()}")
print(f"tv2's channel is {tv2.getChannel()} and volume level is {tv2.getVolume()}")