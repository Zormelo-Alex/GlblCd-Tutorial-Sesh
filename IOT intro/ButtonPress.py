from gpiozero import Button, LED
from signal import pause
from iot_trials import IFTTT_Notification


newNotification = IFTTT_Notification()
notifyMe = IFTTT_Notification("notify")


button = Button(2)
button2 = Button(17)

def button_pressed():
    print("Button one was pressed")
    newNotification.make_request({"name": "Alex"})
    # buzzer.on()
    # buzzer.off()

def button2_pressed():
    print("Button two was pressed")
    notifyMe.make_request()


button.when_pressed = button_pressed
button2.when_pressed = button2_pressed
pause()
