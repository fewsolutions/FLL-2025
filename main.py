from pybricks.parameters import Button, Color
from pybricks.tools import wait

from codes import setup, reset, ready

import Boulders, RemoteControl



#Setup the hub, motors, colour sensor and DriveBase
hub, base, auxL, auxR, colorsensor = setup()

#Setup Color sensor with custom colours
Color.ORANGE = Color(h=5, s=81, v=84)
Color.RED = Color(h=351, s=88, v=56)
Color.YELLOW = Color(h=52, s=72, v=99)
Color.GREEN = Color(h=159, s=57, v=61)
Color.NONE = Color(h=0, s=0, v=0)
Color.BLUE = Color(h=224, s=80, v=52)
Color.CYAN = Color(h=195, s=78, v=72)
if colorsensor != None:
    colorsensor.detectable_colors([Color.ORANGE, Color.RED, Color.YELLOW, Color.GREEN, Color.BLUE, Color.WHITE, Color.CYAN, Color.NONE])

#IMPORTANT
#This is where each code is associated with a letter and colour for the colour sensor
#Format: [("LETTER", Color.COLOUR, Filename.codename)]
codeslist = [
    ("B", Color.YELLOW, Boulders.code1), 
    #("K", Color.RED, Krill.code2), 
    #("C", Color.GREEN, Shark.code3), 
    #("R", Color.WHITE, Radar.code4), 
    #("W", Color.CYAN, Whale.code5), 
    #("S", Color.BLUE, Submarine.code6), 
    ("R", Color.BLACK, RemoteControl.remotecode)
]

selected = 0

def menu(codeslist):
    #sets up some variables
    global selected
    lastsensor = None
    codes = [item[2] for item in codeslist]
    codecount = len(codes) - 1

    #Main menu loop
    while True:
        
        wait(25)

        #print(selected)
        #Display Code Character
        hub.display.char(codeslist[selected][0])

        #Colour sensor attachment detection
        if colorsensor != None:

            #Check what colour the colour sensor can see
            colorsensed = colorsensor.color(surface=True)
            #print(colorsensed)

            #print([item[1] for item in codeslist])

            #Check if this colour is associated with any codes
            if colorsensed in [item[1] for item in codeslist]:
                #print("True")

                #Check if this colour has already been detected and if so don't do anything
                if colorsensed != lastsensor:
                    #Set selected to the code the colour detected is associated with
                    #Edit: added + 1 to the index to fix the index out of range error
                    selected = [item[1] for item in codeslist].index(colorsensed)
  
                    #Remember what the last colour sensed was
                    lastsensor = colorsensed
                    #print(f"Colour sensor used {colorsensed}")
                    continue

            

        else:
            wait(25)

        #Check which buttons have been pressed
        pressed = hub.buttons.pressed()

        if Button.RIGHT in pressed:
            if selected == codecount:
                selected = 0
            else:
                selected = selected + 1
            wait(100)
        elif Button.LEFT in pressed:
            if selected == 0:
                selected = codecount
            else:
                selected = selected - 1
            wait(100)

        elif Button.CENTER in pressed:
            return selected


def main(codeslist):
    while True:
        reset()

        #Run the menu
        codeindex = menu(codeslist)

        ready()

        codeslist[codeindex][2]()

        

if __name__ == "__main__":
    main(codeslist)