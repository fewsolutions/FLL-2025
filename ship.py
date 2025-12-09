from pybricks.tools import wait

def code2():
    # Ship run
    from codes import setup
    hub, b, auxL, auxR, colorsensor = setup()
    b.use_gyro(True)

    b.straight(470)
    b.straight(-114)
    b.turn(-60)
    b.straight(210)
    b.turn(62)
    b.straight(157)
    b.straight(-238)
    b.turn(-35)
    b.straight(305)
    auxL.run_angle(800, 360)
    b.turn(-19)
    auxL.run_angle(800, -110)
    b.straight(50)
    b.straight(-50)
    auxL.run_angle(800, -70)
    b.turn(51)
    b.straight(385)

    b.turn(-40)
    b.turn(65)
    b.use_gyro(False)
    b.straight(700)
    auxL.run_angle(400, 190)



code2()