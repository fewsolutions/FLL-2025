from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    # Boulders run (depricated)
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.straight(378)
    b.turn(-18.55)
    b.straight(470)
    b.turn(68)
    b.use_gyro(False)
    b.turn(-60)
    b.use_gyro(True)
    b.straight(-92)
    b.turn(-90)
    b.straight(-400)
code1()