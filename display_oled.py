from time import sleep

from luma.core.device import device
from luma.core.interface.serial import spi
from luma.oled.device import sh1106
from luma.core.render import canvas
from PIL import ImageFont

class Display:
    """Initialize and control the SH1106 OLED display."""
    def __init__(self):
        serial = spi(
            port = 0,  # SPI0
            device = 0,  # CE0
            gpio_DC = 25,
            gpio_RST = 24)

        self.device = sh1106(
            serial,
            width = 128,
            height = 64,
            rotate = 0 )
            
        self.font12 = ImageFont.truetype('DejaVuSans.ttf',size=12)  # Default font size = 10
        self.count = 0
        
        self.MESSAGES_TITLE = {
            'motion_detected': 'Motion Detected',
            'no_motion': 'Waiting For Motion'
        }
        self.MESSAGES_ACTIVE = {
            'motion_detected': 'Recording now',
            'no_motion': ''
        }

        
    def display_motion(self,motion_detected):
        """
        Display the motion detected on the SH1106 OLED display.
        Args:
            tuple(bool): True to display "Motion detected" on the SH1106 OLED display.
        """
        with canvas(self.device) as draw:
            if motion_detected:
                comment_title = self.MESSAGES_TITLE['motion_detected']
                comment_active = self.MESSAGES_ACTIVE['motion_detected']
                self.count+= 1
            else:
                comment_title = self.MESSAGES_TITLE['no_motion']
                comment_active = self.MESSAGES_ACTIVE['no_motion']
            draw.text((10,5), comment_title, fill='white', font=self.font12)
            draw.text((10,20), comment_active, fill='white')
            draw.text((10,40), f"Detected Count : {self.count}", fill='white')
        sleep(1)


    def destroy(self):
        """Close the display."""
        try:
            self.device.clear()
        except Exception:
            pass