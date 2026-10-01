from spike import PrimeHub, Motor
from spike.control import wait_for_seconds

hub = PrimeHub()

left_motor = Motor("A")
right_motor = Motor("B")

WHEEL_DIAMETER_CM = 5.6
PI = 3.1416

def drive_cm(cm, speed=50):
    degrees = int((cm / (PI * WHEEL_DIAMETER_CM)) * 360)
    left_motor.run_for_degrees(degrees, speed=speed)
    right_motor.run_for_degrees(degrees, speed=speed)

def turn_right_90():
    left_motor.run_for_degrees(180, speed=40)
    right_motor.run_for_degrees(-180, speed=40)

def turn_left_90():
    left_motor.run_for_degrees(-180, speed=40)
    right_motor.run_for_degrees(180, speed=40)

drive_cm(100, speed=50)
turn_right_90()
drive_cm(50, speed=45)
drive_cm(100, speed=50)
turn_left_90()
drive_cm(50, speed=45)

hub.light_matrix.show_image("HAPPY")
