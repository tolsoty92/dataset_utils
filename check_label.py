import os
from shutil import copyfile

for i in range(9):
    x = str(i)
    IMAGES_DIR = "/home/user/Documents/create_num_dataset/ip_video/"+x+"/"+x+"_image/"
    LABELS_LST = "./labels/"
    LABELED_IMGS_DIR = "./labeled_images/"

    labels_lst = os.listdir(LABELS_LST)

    for label in labels_lst:
        img_num = label[:-4]
        img_name = img_num+".jpg"
        if img_name in os.listdir(IMAGES_DIR):
                copyfile(IMAGES_DIR+img_name, LABELED_IMGS_DIR+img_name)
