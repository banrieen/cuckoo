""" Camera driver

    author: haiyuan
    Date:2019-07-02
"""

from picamera import PiCamera
from time import sleep



def capture_picture(camera,inter=5,filepath="/home/pi/workspace"):
    for i in range(inter):
        camera.capture(filepath+"/image0%s.jpg" % i)

def record_mov(camera,inter=10,filepath="/home/pi/workspace"):
    camera.start_recording(filepath+"/video_abc.h264" )
    sleep(inter)
    camera.stop_recording()
    
def main():
    camera = PiCamera()
    camera.rotation = 180
    camera.start_preview()
    capture_picture(camera,inter=5,filepath="/home/pi/workspace")
    record_mov(camera,inter=10,filepath="/home/pi/workspace")
    sleep(10)
    camera.stop_preview()

if __name__ == "__main__":
    main()
