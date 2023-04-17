
from wpilib import Spark,Encoder
from wpilib.drive import DifferentialDrive

class Drivetrain:
        def __init__(self):
            self.left_motor = Spark(0)
            self.right_motor = Spark(1)
            self.drivetrain = DifferentialDrive(self.left_motor, self.right_motor)
            self.left_encoder = Encoder(4, 5)
            self.right_encoder = Encoder(6, 7)


        def move(self, forward, rotate):
            self.drivetrain.arcadeDrive(forward,rotate)

        def stop(self):
            self.right_motor.stopMotor()
            self.left_motor.stopMotor()

        def reset_encoders(self):
            self.left_encoder.reset()
            self.right_encoder.reset()

