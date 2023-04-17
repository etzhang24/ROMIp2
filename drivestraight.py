
class Drivestraight:
    def __init__(self, drivetrain):
        self.drivetrain = drivetrain



    def run(self):
        x=0
        print(f"left: {self.drivetrain.left_encoder.get()}")
        print(f"right: {self.drivetrain.right_encoder.get()}")
        if self.drivetrain.left_encoder.get() < self.drivetrain.right_encoder.get():
            self.drivetrain.move(0.2,0.3)
        elif self.drivetrain.right_encoder.get() < self.drivetrain.left_encoder.get():
            self.drivetrain.move(-0.2,0.3)
        elif self.drivetrain.right_encoder.get() > 10000:
            self.drivetrain.stop()
        else:
            self.drivetrain.move(0, 0.3)

