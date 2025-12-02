from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    # Boulders run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.turn(20)
    wait(1)
    b.turn(-40)
    b.turn(20)
    b.straight(10)
    
    

code1()