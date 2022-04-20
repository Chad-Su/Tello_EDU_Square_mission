from tello import *
start()
power = get_battery()
print("Power Level:",power,"%")

takeoff()
up(50)
for i in range (1,5):
    flip_left()
land()

print(tello_ip)