from pybricks.parameters import Stop, Button, Port, Direction, Color
from pybricks.tools import wait
from pybricks.pupdevices import Remote, Motor
from pybricks.robotics import DriveBase
from codes import setup

hub, b, auxL, auxR, colorsensor = setup()
def remotecode():
    r = Remote()
    mode = 1
    r.light.on(Color.GREEN)
    auxL.reset_angle(angle=0)
    auxR.reset_angle(angle=0)

    while True:
        pressed = r.buttons.pressed()

        if Button.CENTER in pressed:
            if mode == 1:
                mode = 2
                r.light.on(Color.ORANGE)
            else:
                mode = 1
                r.light.on(Color.GREEN)

        if Button.LEFT in pressed and Button.RIGHT in pressed:
            b.reset()
            auxL.reset_angle(angle=0)
            auxR.reset_angle(angle=0)
            wait(100)

        if mode == 1:

            if Button.LEFT_PLUS in pressed:
                b.straight(10, then=Stop.NONE)

            elif Button.LEFT_MINUS in pressed:
                b.straight(-10, then=Stop.NONE)

            elif Button.RIGHT_PLUS in pressed:
                b.turn(1
                
                
                , then=Stop.NONE)
            
            elif Button.RIGHT_MINUS in pressed:  
                b.turn(-1, then=Stop.NONE)

            else:
                b.stop()




            if Button.LEFT in pressed and Button.RIGHT not in pressed:
                print(f"b.straight({b.distance()})")
                wait(100)

            if Button.RIGHT in pressed and Button.LEFT not in pressed:
                print(f"b.turn({b.angle()})")
                wait(100)

        if mode == 2:

            if Button.LEFT_PLUS in pressed:
                auxL.run(500)

            elif Button.LEFT_MINUS in pressed:
                auxL.run(-500)

            else:
                auxL.stop()

            if Button.RIGHT_PLUS in pressed:
                auxR.run(100)
            
            elif Button.RIGHT_MINUS in pressed:
                auxR.run(-100)

            else:
                auxR.stop()

            if Button.LEFT in pressed and Button.RIGHT not in pressed:
                print(f"auxL.run_angle(400, {auxL.angle()})")
                wait(100)

            if Button.RIGHT in pressed and Button.LEFT not in pressed:
                print(f"auxR.run_angle(400, {auxR.angle()})")
                wait(100)

        wait(100)

remotecode()