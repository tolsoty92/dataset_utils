import os
from shutil import copyfile

IMAGES_DIR = "./images/"
LABELS_LST = "./labels/"
LABELED_IMGS_DIR = "./labeled_images/"

labels_lst = os.listdir(LABELS_LST)

for label in labels_lst:
	img_num = label[:-4]
	img_name = img_num+".jpg"
	copyfile(IMAGES_DIR+img_name, LABELED_IMGS_DIR+img_name)
