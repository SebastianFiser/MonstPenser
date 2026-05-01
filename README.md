# MonstPenser
A monster dispensing wall - hangable tool with oled screen and buttons! up to 3 cartridges if you wan to separate your flavours

# WHAT IS THIS ??

MonsterDispenser is a wall-mounted vending unit built for one purpouse - fetting you a cold monster / *energy dring of the same size* at the press of the button.

It holds 3 gravity-fed tracks of monster cans . **If some people want to separate flavours** Each track has its own button. Hit it, and the servo gates releases, and a can rolls out! A smalll 128x 64 OLED screen in front shows how many cans are left in each slot **IN REAL TIME** mindblowing i know.  You sadly restock yourself, and im defo not paying for it.

# Features
•🟢 ***3 independent slots** - One per monster flavour or just triple the amount of one
•🖥️ **OLED inventory display** - shows live count per slot
•🔘 **3 dedicated bttons** - one press, one slot
•⚙️ **Servo gate mechanism** - gravity fed tracks, servo holds and releases cans
•🧠 **Raspberry Pi Pico** - runs the whole thing
•🔌 **Custom PCB** (kicad designed) - clean wiring = no mess
•📦 **OPEN SOURCE** - build one yourself

# How it works
```sh
[Can stack] -> [Gravity Track] -> [Servo Gate] -> [Dispensed Can]
                                        ↑
                                   [Button Press]
                                        ↑
                                [Raspberry Pi Pico]
                                        ↑
                                  [Oled Display]                                             
```

1. Cans are loaded into the 3 gravity-fed tracks from the top/back
2. A servo motor acts as a gate at the bottom of eatch track
3. at the press of an button, Pico triggers the coresponding servo to open, releasing one can
4. The pico subtracts the can from cout in the slot and updates OLED display
5. When a slot is empty button is disabled, and screen shows empty

# Parts list 
| **Component**|**Purpouse**|**Cost**|
|---|---|---|
|Raspberry Pi Pico| Microcontroller/ Brain |~$5|
|128x64 OLED display (I2C)|Inventroy Screen|~$5|
|SG90 Servo Mototrs (3x) | Can gate Mecahnism|~$10|
|CUSTOM PCB| (JLCPCB/PCBWAY)| Clean wiring |~$10|
|Wood / acrylic shield / building mats| Enclosure|~$15|
|Miscs(wire, screws, brackets)|Assemby (the manual one)|~$10
**ESTIM. total ~$58?**
// 35 miutes the recorsing didnt work i want to jump
Repo structure
```Code
MonsterDispenser/
├── firmware/
│   └── main.py #Pico firmwae
├── pcb/
|   ├── schematic.kicad_sch
|   ├── layout.kicad_pcb
|   └── gerbers/ #Ready to order files
├── enclosure/
|    └──buuild_notes.md #Dimentioons and assembly guide
├── docs/
|    └── wiring-diagram.png
└── README.png
```

# Wiring overwiew
Soon (the pcb aint even done)

# Craft guide
-todo
# Firmware
- work not started
# Future ideas
-none

# Built for
This project is being built as part of **Hack club Fallout** 
BUT also for people that dont want to have their preciosly bought drinks brought home chaotiucly stored

# License
MIZT- build it, mod it, ship it.
