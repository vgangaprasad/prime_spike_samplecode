from hub import port

import runloop, motor_pair, sys

# cm, this is a constant for your robot
WHEEL_CIRCUMFERENCE = 17.5

# input must be in the same unit as WHEEL_CIRCUMFERENCE
def degreesForDistance(distance_cm):
# Add multiplier for gear ratio if needed
  return int((distance_cm/WHEEL_CIRCUMFERENCE) * 360)

async def main():
 # Drive Base 1
  motor_pair.pair(motor_pair.PAIR_1, port.C, port.D)
  await motor_pair.move_for_degrees(motor_pair.PAIR_1, degreesForDistance(10), 0)
  sys.exit("Finished")

runloop.run(main())
