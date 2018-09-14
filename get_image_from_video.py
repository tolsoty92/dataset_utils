import cv2
import os

num = "9"

VIDEO_DIR = "/home/user/Documents/create_num_dataset/ip_video/"+num+"/"
os.mkdir("/home/user/Documents/create_num_dataset/ip_video/"+num+"/"+num+"_image/")
IMAGES_DIR = "/home/user/Documents/create_num_dataset/ip_video/"+num+"/"+num+"_image/"

video_lst = os.listdir(VIDEO_DIR)

counter = 0

for video in video_lst:
	stream = cv2.VideoCapture(VIDEO_DIR+video)
	while stream.isOpened():
		ret, img = stream.read()
                
		if ret:
                        img = cv2.resize(img, (640, 360))
			cv2.imwrite(IMAGES_DIR+num+"_"+str(counter)+".jpg", img)
			print(counter)
			counter += 1				
		else:
			break

		
