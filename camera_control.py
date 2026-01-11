import time
from datetime import datetime
import os

import libcamera
from luma.core.device import device
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder

class CameraControl():
    """Control the camera for initialization, image capture, and video recording."""
    def __init__(self):
        self.picam2 = Picamera2()
        self.video_config = self.picam2.create_video_configuration()
        self.video_config['transform'] = libcamera.Transform(hflip=1,vflip=1)
        self.image_config = self.picam2.create_preview_configuration()
        self.image_config['transform'] = libcamera.Transform(hflip=1,vflip=1)
        self.encoder = H264Encoder(bitrate=1000000)
        self.recording_time = 10
        
        os.makedirs('Capture/',exist_ok=True)


    def capture_video(self):
        """
        Record a video clip and save it to a timestamped file.
        Returns:
            tuple[datetime, str]: Capture time and output file path.
        """
        self.picam2.configure(self.video_config)
        record_time = datetime.now()
        record_time_str = record_time.strftime("%Y%m%d_%H%M%S")
        output_video_file ="Capture/" + record_time_str + ".h264"

        self.picam2.start_recording(self.encoder, output_video_file)
        time.sleep(self.recording_time)
        self.picam2.stop_recording()
        return record_time,output_video_file


    def capture_image(self):
        """
        Capture the image from the camera and record it in a file.
        Returns:
            tuple[datetime, str]: Capture time and output file path.
        """
        self.picam2.configure(self.image_config)
        capture_time = datetime.now()
        capture_time_str = capture_time.strftime("%Y%m%d_%H%M%S")
        output_image_file ="Capture/" + capture_time_str + ".jpg"

        self.picam2.start(show_preview=True)
        time.sleep(1)  # wait for camera adjustment
        self.picam2.switch_mode_and_capture_file(self.image_config, output_image_file)
        self.picam2.stop()
        return capture_time,output_image_file


    def destroy(self):
        """Stop camera activity and close resources."""
        try:
            self.picam2.stop_recording()
        except Exception:
            pass

        try:
            self.picam2.stop_preview()
        except Exception:
            pass

        self.picam2.close()