from pybricks.parameters import Stop
from pybricks.tools import wait, multitask, run_task


# Reset
from codes import setup
hub, b, auxL, auxR, colorsensor = setup()

auxL.run_target(400, 0)
auxR.run_target(400, 0)
