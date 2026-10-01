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

def gyro_turn_right(target_angle=90, speed=25):
    hub.motion_sensor.reset_yaw_angle()
    left_motor.start(speed)
    right_motor.start(-speed)

    while hub.motion_sensor.get_yaw_angle() < target_angle:
        wait_for_seconds(0.01)

    left_motor.stop()
    right_motor.stop()

def gyro_turn_left(target_angle=-90, speed=25):
    hub.motion_sensor.reset_yaw_angle()
    left_motor.start(-speed)
    right_motor.start(speed)

    while hub.motion_sensor.get_yaw_angle() > target_angle:
        wait_for_seconds(0.01)

    left_motor.stop()
    right_motor.stop()

drive_cm(100, speed=50)
gyro_turn_right(90, speed=25)
drive_cm(50, speed=45)
drive_cm(100, speed=50)
gyro_turn_left(-90, speed=25)
drive_cm(50, speed=45)

hub.light_matrix.show_image("HAPPY")
