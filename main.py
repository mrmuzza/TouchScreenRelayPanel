from guizero import App, PushButton, Slider, Text
from PIL import Image
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# path = '/home/ron/TouchScreenRelayPanel/'
path = '/home/pi/TouchScreenRelayPanel/'
leftlights_state = 0
rightlights_state = 0
waterpump_state = 0
waterheat_state = 0
inverter_state = 0
doorlights_light_state = 0
kitchenlights_state = 0
extract_state = 0
sidelights_state = 0

def leftlights_callback():
    global leftlights_state, leftlights_button
    if leftlights_state == 0:
        leftlights_state = 1
        leftlights_button.image = path + 'leftlights_on.png'
        GPIO.setup(40, GPIO.OUT)
        GPIO.output(40, GPIO.LOW)
    else:
        leftlights_state = 0
        leftlights_button.image = path + 'leftlights_off.png'
        GPIO.setup(40, GPIO.OUT)
        GPIO.output(40, GPIO.HIGH)

def rightlights_callback():
    global rightlights_state, rightlights_button
    if rightlights_state == 0:
        rightlights_state = 1
        rightlights_button.image = path + 'rightlights_on.png'
        GPIO.setup(36, GPIO.OUT)
        GPIO.output(36, GPIO.LOW)
    else:
        rightlights_state = 0
        rightlights_button.image = path + 'rightlights_off.png'
        GPIO.setup(36, GPIO.OUT)
        GPIO.output(36, GPIO.HIGH)


def waterpump_callback():
    global waterpump_state, waterpump_button
    if waterpump_state == 0:
        waterpump_state = 1
        waterpump_button.image = path + 'waterpump_on.png'
        GPIO.setup(31, GPIO.OUT)
        GPIO.output(31, GPIO.LOW)
    else:
        waterpump_state = 0
        waterpump_button.image = path + 'waterpump_off.png'
        GPIO.setup(31, GPIO.OUT)
        GPIO.output(31, GPIO.HIGH)


def waterheat_callback():
    global waterheat_state, waterheat_button
    if waterheat_state == 0:
        waterheat_state = 1
        waterheat_button.image = path + 'waterheat_on.png'
        GPIO.setup(32, GPIO.OUT)
        GPIO.output(32, GPIO.LOW)
    else:
        waterheat_state = 0
        waterheat_button.image = path + 'waterheat_off.png'
        GPIO.setup(32, GPIO.OUT)
        GPIO.output(32, GPIO.HIGH)

def inverter_callback():
    global inverter_state, inverter_button
    if inverter_state == 0:
        inverter_state = 1
        inverter_button.image = path + 'inverter_on.png'
        GPIO.setup(39, GPIO.OUT)
        GPIO.output(39, GPIO.LOW)
    else:
        inverter_state = 0
        inverter_button.image = path + 'inverter_off.png'
        GPIO.setup(39, GPIO.OUT)
        GPIO.output(39, GPIO.HIGH)

def doorlights_callback():
    global doorlights_state, doorlights_button
    if doorlights_state == 0:
        doorlights_state = 1
        doorlights_button.image = path + 'doorlights_on.png'
        GPIO.setup(38, GPIO.OUT)
        GPIO.output(38, GPIO.LOW)
    else:
        doorlights_state = 0
        doorlights_button.image = path + 'doorlights_off.png'
        GPIO.setup(38, GPIO.OUT)
        GPIO.output(38, GPIO.HIGH)

def kitchenlights_callback():
    global kitchenlights_state, kitchenlights_button
    if kitchenlights_state == 0:
        kitchenlights_state = 1
        kitchenlights_button.image = path + 'kitchenlights_on.png'
        GPIO.setup(33, GPIO.OUT)
        GPIO.output(33, GPIO.LOW)
    else:
        kitchenlights_state = 0
        kitchenlights_button.image = path + 'kitchenlights_off.png'
        GPIO.setup(33, GPIO.OUT)
        GPIO.output(33, GPIO.HIGH)

def extract_callback():
    global extract_state, extract_button
    if extract_state == 0:
        extract_state = 1
        extract_button.image = path + 'extract_on.png'
        GPIO.setup(35, GPIO.OUT)
        GPIO.output(35, GPIO.LOW)
    else:
        extract_state = 0
        air_button.image = path + 'extract_off.png'
        GPIO.setup(35, GPIO.OUT)
        GPIO.output(35, GPIO.HIGH)

def sidelights_callback():
    global sidelights_state, sidelights_button
    if sidelights_state == 0:
        sidelights_state = 1
        sidelights_button.image = path + 'sidelights_on.png'
        GPIO.setup(37, GPIO.OUT)
        GPIO.output(37, GPIO.LOW)
    else:
        sidelights_state = 0
        sidelights_button.image = path + 'sidelights_off.png'
        GPIO.setup(37, GPIO.OUT)
        GPIO.output(37, GPIO.HIGH)

def screen_brightness():
    global slider
    print(slider.value)
    bl.set_brightness(str(slider.value))



app = App(title="Keypad example", width=480, height=320, layout="grid")
app.bg='black'
leftlights_button = PushButton(app, command=leftlights_callback, grid=[0,0], align='left', image = path + ‘leftlights_off.png')
rightlights_button = PushButton(app, command=rightlights_callback, grid=[2,0], align='left',image = path + ‘rightlights_off.png')
waterpump_button  = PushButton(app, command=waterpump_callback, grid=[1,3], align='left',image = path + 'waterpump_off.png')
waterheat_button  = PushButton(app, command=waterheat_callback, grid=[0,3], align='left',image = path + 'waterheat_off.png')
inverter_button  = PushButton(app, command=inverter_callback, grid=[1,1], align='left',image = path + ‘inverter_off.png')
doorlights_button = PushButton(app, command=doorlights_callback, grid=[1,0], align='left', image = path + ‘doorlights_off.png')
kitchenlights_button = PushButton(app, command=kitchenlights_callback, grid=[2,1], align='left',image = path + ‘kitchenlights_off.png')
extract_button  = PushButton(app, command=extract_callback, grid=[2,3], align='left',image = path + ‘extract_off.png')
sidelights_button  = PushButton(app, command=sidelights_callback, grid=[0,1], align='left',image = path + ’sidelights_off.png')


# slider = Slider(app, command=screen_brightness, grid=[0,2,3,2], align='left', start=30, end=255)
# slider.value='255'
# slider.resize(320, 40)
# slider.text_color='white'
# slider.bg='black'

def main():
    app.tk.attributes("-fullscreen",True)
    app.tk.config(cursor='none')
    app.display()

if __name__ == '__main__':
    main()



