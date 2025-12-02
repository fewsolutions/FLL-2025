from pybricks.parameters import Stop
from pybricks.tools import wait

def code1():
    # Boulders run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.straight(272)
    b.turn(-32.5)
    b.straight(688)
    b.turn(-55)
    b.straight(135)
    b.settings(straight_speed=500)
    b.turn(47)
    b.settings(straight_speed=500)
    b.straight(-250)
    auxL.run_angle(500, -200)
    auxL.run_angle(500, 200)
    b.straight(90)
    b.turn(120)
    b.straight(200)
    b.turn(-60)
    b.straight(-45)
    b.turn(-99)
    b.straight(-480)
    b.turn(52)
    auxR.run_angle(100, -270)
    auxR.run_angle(400, 190)
    b.turn(16)
    


    auxL.run_target(400, 0)
    auxR.run_target(400, 0)

    
code1()