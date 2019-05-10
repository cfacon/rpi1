#import cv2, subprocess, sys
import subprocess, sys

process = subprocess.Popen( ["mjpg_streamer", "-i", "/usr/lib/input_uvc.so -d /dev/video0 -y -r 320x240 -f 12", "-o", "/usr/lib/output_http.so -p 8090 -w ./www"]
                          )

#process = subprocess.Popen( ["cvlc", "v4l2:///dev/video0", "--sout", "#transcode{vcodec=MJPG,vb=500,width=352,height=288}:duplicate{dst=std{access=http{mime=multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a},mux=mpjpeg,dst=:9090/webcam.mjpg}}"]
#                          )

print("Video capture started")
