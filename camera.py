import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
import numpy as np

class VideoCamera(object):
    def __init__(self, flip = False):
        self.vs = None
        self.flip = flip

    def __del__(self):
        if self.vs is not None:
            self.vs.stop()

    def start(self, flip = False):
        if self.vs is None:
            self.vs = PiVideoStream().start()
            self.flip = flip
            time.sleep(2.0)
        
    def stop(self):
        if self.vs is not None:
            self.vs.stop()
            self.vs = None
        
    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def get_frame(self):
        if self.vs is None:
            return
        frame = self.flip_if_needed(self.vs.read())
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()



