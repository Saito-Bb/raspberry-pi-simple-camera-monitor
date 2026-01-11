from time import sleep

from gpiozero import Button,LED,MotionSensor

class InputDevices:
    """Initialize and control input devices connected to GPIO pins."""
    def __init__(self):
        self.BUTTON_PIN = (17)
        self.MOTION_PIN = (27)
        self.motion_sensor = MotionSensor(self.MOTION_PIN)


    def motion_monitoring(self):
        """Motion monitoring function."""
        return self.motion_sensor.motion_detected


    def destroy(self):
        """Close input devices."""
        try:
            self.motion_sensor.close()
        except Exception:
            pass

class OutputDevices():
    """Initialize and control output devices connected to GPIO pins."""
    def __init__(self):
        self.LED_PIN = (18)
        self.led = LED(self.LED_PIN)


    def led_on(self,state):
        """
        Turn the LED on or off based on the given state.

        Args:
            state(bool): True to turn on, False to turn off.
        """
        if state == True:
            self.led.on()
        elif state == False:
            self.led.off()


    def destroy(self):
        """Close all output devices."""
        try:
            self.led.close()
        except Exception:
            pass
