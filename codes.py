from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis, Icon
from pybricks.robotics import DriveBase


#Setup the hub with the top side (with the USB) as the X axis and the front side (with the buttons) as the Y axis
hub = PrimeHub(top_side=Axis.Z, front_side=Axis.Y)
hub.display.orientation(Side.RIGHT)

#Set the stop button to the bluetooth button 
#This will stop the ENTIRE program, including the main code which includes the menu, but this can be fixed by pressing the centre button when the square shown on the Prime Hub display
hub.system.set_stop_button(Button.BLUETOOTH)

#Swap Clockwise and Counterclockwise here if robot is driving backward when it should be driving forward
driveL = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
driveR = Motor(Port.E, positive_direction=Direction.CLOCKWISE)

#Setup auxiliary motors and colour sensor
auxL = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
auxR = Motor(Port.F, positive_direction=Direction.CLOCKWISE)

cs_activate = True  #Set to False if you dont want to use colour sensor
try:
    colorsensor = ColorSensor(Port.D)
    if cs_activate:
        pass
    else:
        colorsensor.lights.off()
        colorsensor = None
    
except OSError as e:
    if e.errno == 19:  # OSError 19 is "no such device"
        print("Color Sensor Disconnected")
        colorsensor = None  # Set to None or handle accordingly
    else:
        raise  # Re-raise the exception if it's a different OSError



#Setup the DriveBase with the left motor as driveL, the right motor as driveR, the wheel diameter as 57.25mm and the axle track (width between the middle of the wheels) as 99.09mm
base = DriveBase(left_motor=driveL, right_motor=driveR, wheel_diameter=57.25, axle_track=99.7)
base.use_gyro(False)
base.settings(straight_speed=750, straight_acceleration=500, turn_rate=200, turn_acceleration=200)

def setup():
    #Return the hub, left aux motor, right aux motor, colour sensor and DriveBase in that order so it can be referenced and used in the main code as well as other auxiliary codes to ensure every code uses the same parameters
    return hub, base, auxL, auxR, colorsensor

def reset():
    base.use_gyro(False)
    hub.imu.reset_heading(0)
    auxL.run_target(400, 0)
    auxR.run_target(400, 0)
    if colorsensor != None:
        colorsensor.lights.on(100)
    hub.light.on(Color.GREEN)

def ready():
    if colorsensor != None:
        colorsensor.lights.off()

    hub.imu.reset_heading(0)
    base.use_gyro(True)
    hub.light.off()
    hub.display.icon(Icon.UP)
    
