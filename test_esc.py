from machine import Pin, PWM
import time

ESC_PIN = 17




class RCCar:
    def __init__(self):
        self.esc = PWM(ESC_PIN)
        self.esc.freq(50)
        
    def set_pulse(self, microseconds: int) -> None:
            """Sets a PWM duty cycle based on a pulse width.
            
            Args:
                microseconds: Duration of the high pulse in microseconds (1000-2000 typical).
            """
            duty = int(microseconds / 20000 * 65535)
            self.esc.duty_u16(duty)

    def forward(self) -> None:
        self.set_pulse(1550)
        
    def stop(self) -> None:
        self.set_pulse(1500)

car = RCCar()

i = 0

while i < 10000:
    car.stop()
    i += 1

car.forward()