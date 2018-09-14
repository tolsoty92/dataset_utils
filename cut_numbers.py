import cv2
import os
import csv

CSV = "./labels.csv"
CUT_IMAGES = "./cuted/"
IMAGE_DIR = "./images/"


count = 0

with open(CSV, 'rb') as csvfile:
    data = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in data:
        if count != 0:
            row = row[0].split(",")
            img_name = IMAGE_DIR+row[0]
            #print(img_name)
            x_min, y_min = int(row[4]), int(row[5])
            width, height = int(row[6])-x_min, int(row[7])-y_min
            img = cv2.imread(img_name)
            #print(img)
            num = img[y_min:y_min+height, x_min:x_min+width]
            num = cv2.cvtColor(num, cv2.COLOR_BGR2GRAY)
            print(CUT_IMAGES+img_name)
            cv2.imwrite(CUT_IMAGES+row[0][0]+"/"+row[0], num)
        count += 1
        print(count)
