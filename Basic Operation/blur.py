import numpy as np
import cv2

img = cv2.imread('../data/lane.jpg')
#print(type(img)) #checking if any error occured
#Gausian Blur
while(True):
	kernel = tuple(map(int,input('Enter kernel value in format x,x :').split(',')))
	processed_img = cv2.GaussianBlur(img,kernel,0)
	canny_image = cv2.Canny(processed_img,50,150)
	cv2.imshow('Blur effect in canny',canny_image)
	cv2.waitKey(1)
