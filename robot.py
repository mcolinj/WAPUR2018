import wpilib
import ctre

class WAPURBot(wpilib.IterativeRobot):
    def robotInit(self):
        self.l_motor = ctre.CANTalon(3)
        self.l_motor2 = ctre.CANTalon(4)
        self.r_motor = ctre.CANTalon(1)
        self.r_motor2 = ctre.CANTalon(2)
        self.robot_drive = wpilib.RobotDrive(self.l_motor, self.l_motor2, self.r_motor, self.r_motor2)
        self.stick = wpilib.Joystick(0)

    def teleopPeriodic(self):
        self.robot_drive.arcadeDrive(self.stick)
        print(self.l_motor.get())

    def autonomousInit(self):
        print("Auto Init")

    def autonomousPeriodic(self):
        self.l_motor.set(1)
        self.r_motor.set(-1)

if __name__ == '__main__':
    wpilib.run(WAPURBot, physics_enabled=True)

