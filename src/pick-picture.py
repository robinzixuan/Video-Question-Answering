import cv2 as cv
import skvideo
from skvideo import io
import os
 
def vidio_frame_extract(video_path,save_path,index):
    capture = skvideo.io.vreader(video_path + '/' + index)
    for frame in capture:
        frame = cv.cvtColor(frame,cv.COLOR_RGB2BGR)
        cv.imshow("frame",frame)
        save_frame = "{}/{}.jpg".format(save_path, index)
        cv.imwrite(save_frame,frame)
        break
 
if __name__ == "__main__":
    video_path = "/Volumes/SEAGATE/videos"
    save_path = "/Users/robin/Downloads/video/result"
    files = os.listdir(video_path)
    for index in files:
        if len(index.split('.avi')) > 1:
            vidio_frame_extract(video_path, save_path, index)