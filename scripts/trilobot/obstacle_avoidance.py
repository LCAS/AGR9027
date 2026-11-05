# This is a basic example of reactive obstacle avoidance using Trilobot's ultrasound
# distance sensor only (no camera). The robot drives forward and, whenever something
# is detected closer than AVOID_DISTANCE, it stops and turns until the way ahead is
# clear again, then carries on driving forward.
# Stop the example by pressing button A.

import time
from trilobot import Trilobot, BUTTON_A

print("Trilobot Example: Obstacle Avoidance\n")

tbot = Trilobot()

AVOID_DISTANCE = 30    # distance in cm at which the robot starts avoiding an obstacle
DRIVE_SPEED = 0.6      # speed used to drive forward
TURN_SPEED = 0.6       # speed used to turn away from an obstacle
TURN_TIME = 0.4        # seconds spent turning before checking the distance again

try:
    while not tbot.read_button(BUTTON_A):

        try:
            distance = tbot.read_distance(timeout=50, samples=3)
        except Exception as e:
            # lgpio can fail with 'bad event request' if the echo pin is still claimed; stop for safety
            print("Distance read failed:", e)
            tbot.disable_motors()
            time.sleep(0.1)
            continue
        print("Distance is {:.1f} cm".format(distance))

        if distance < AVOID_DISTANCE:
            print("Obstacle detected! Turning...")
            tbot.turn_right(TURN_SPEED)
            time.sleep(TURN_TIME)
        else:
            tbot.forward(DRIVE_SPEED)
except KeyboardInterrupt:
    pass
finally:
    tbot.disable_motors()
print("Done")
