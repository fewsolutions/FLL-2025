from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    # Boulders run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.straight(423)
    b.turn(-38)
    b.straight(435)
    b.turn(-30)
    b.straight(60)
    b.turn(-120)


code1()