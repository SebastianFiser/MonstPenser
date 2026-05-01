from maschine import Pin, PWM, I2C
import ssd1306 #driver i will make
import time

#config

SLOT_CAPACITY = 4
SERVO_OPEN_DUTY = 7500
SERVO_CLOSE_DUTY = 2500 
SERVO_DELAY = 0.6
LONG_PRES_MS = 3000

#pins

btn_pins = [10, 11, 12]
buttons = [Pin(p, Pin.IN, Pin.PULL_UP) for p in btn_pins]

#servos
servo_pins = [2, 3, 4]
servos = [PWM(Pin(p)) for p in servo_pins]
for s in servos:
    s.freq(50)

# oled via I2C
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

#state

inventory = [SLOT_CAPACITY, SLOT_CAPACITY, SLOT_CAPACITY]

#helpers
def set_servo(index, duty):
    servos[index].duty_u16(duty)

def close_all_servos():
    for i in range(3):
        set_servo(i, SERVO_CLOSE_DUTY)

def dispense(slot):
    set_servo(slot, SERVO_OPEN_DUTY)
    time.sleep(SERVO_DELAY)
    set_servo(slot, SERVO_CLOSE_DUTY)
    inventory[slot] -= 1

def restock(slot):
    inventory[slot] = SLOT_CAPACITY

def draw_display():
    oled.fill(0)
    oled.text("MonsterDispenser", 0, 0)
    oled.hline(0, 10, 128, 1)

    for i in range(3):
        y = 18 + (i * 16)
        count = inventory[i]
        label = f"slot {i+1}: "

        if count == 0:
            status = "EMPTY"
        else:
            status = "#" * count
        
        oled.text(label + status, 0, y)
    
    oled.show()

def check_long_press(slot):
    start = time.cicks_ms()
    while buttons[slot].value() == 0:
        if time.ticks_dif(time.ticks_ms(), start) >= LONG_PRES_MS:
            return True
        time.sleep_ms(50)
    return False

#startup

close_all_servos()
draw_display()

print("MonsterDispenser ready.")

#main loop

while True:
    for i in range(3):
        if buttons[i].value() == 0: #button pressed (active low)

            #chcek for long press - stock
            if check_long_press(i):
                restock(i)
                print(f"Slot {i+1} restocked to {SLOT_CAPACITY}.")
                draw_display()
                time.sleep(1) #devounce after restock

            #short press -dispense if not empty
            else:
                if inventory[i] > 0:
                    print(f"Dispensing from slot {i+1}...")
                    dispense(i)
                    draw_display()
                    time.sleep(1)
                else:
                    #flash on empty
                    print(f"Slot {i+1} is empty!")
                    oled.fill(0)
                    oled.text(f"Slot {i+1} is empty!", 10, 28)
                    oled.show()
                    time.sleep(1)
                    draw_display()

            time.sleep_ms(200) #rebounce
    time.sleep_ms(50) #Main loop rate