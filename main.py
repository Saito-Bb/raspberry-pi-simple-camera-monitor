from time import sleep

import in_out_sensor
import display_oled
import camera_control
import event_logger


class Main:
    """Main class to run the application."""
    def __init__(self):
        self.in_sensor = in_out_sensor.InputDevices()
        self.out_sensor = in_out_sensor.OutputDevices()
        self.display = display_oled.Display()
        self.camera = camera_control.CameraControl()
        self.event_logger = event_logger.EventLogger()


    def loop(self):
        """
        Main loop to monitor motion sensor state changes.
        """
        motion_current_state = False
        motion_previous_state = False
        self.display.display_motion(False)

        while True:
            motion_current_state = self.in_sensor.motion_monitoring()

            # detect motion start (OFF -> ON transition)
            if motion_current_state is True and motion_previous_state is False:
                motion_previous_state = True
                self.out_sensor.led_on(True)
                self.display.display_motion(True)
                capture_time, capture_file = self.camera.capture_video()
                capture_time_str = capture_time.strftime("%Y/%m/%d %H:%M:%S")
                self.event_logger.event_logging(capture_time,capture_file)

            # detect motion stop(ON -> OFF transition)
            elif motion_current_state is False and motion_previous_state is True:
                self.out_sensor.led_on(False)
                self.display.display_motion(False)
                motion_previous_state = False
            sleep(1)


    def destroy(self):
        """Close all open connections."""
        self.in_sensor.destroy()
        self.out_sensor.destroy()
        self.display.destroy()
        self.camera.destroy()
        self.event_logger.close()


if __name__ == '__main__':
    main = Main()
    try:
        main.loop()
    except KeyboardInterrupt:
        main.destroy()



