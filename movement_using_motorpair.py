from spike import PrimeHub, MotorPair
from spike.control import wait_for_seconds

hub = PrimeHub()

drive = MotorPair("A", "B")

# 100 cm straight
drive.move_for_degrees(1000, steering=0, speed=50)

# turn right and move 50 cm
drive.start(100, 40)
wait_for_seconds(0.6)
drive.stop()
drive.move_for_degrees(500, steering=0, speed=45)

# move 100 cm
drive.move_for_degrees(1000, steering=0, speed=50)

# turn left and move 50 cm
drive.start(-100, 40)
wait_for_seconds(0.6)
drive.stop()
drive.move_for_degrees(500, steering=0, speed=45)

hub.light_matrix.show_image("HAPPY")
