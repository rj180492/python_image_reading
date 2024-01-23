import cv2
from matplotlib import pyplot as plt
import numpy as np
read_image1=cv2.imread('images/Image1.jpeg')
print(read_image1)
print(read_image1.shape)

#first pixel in image
# print(read_image1[0][0])
# cv2.imshow('image',read_image1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#open cv has BGR and matplotlib has RGB

image_rgb=cv2.cvtColor(read_image1,cv2.COLOR_BGR2RGB)
#plt.imshow(image_rgb) #works in jupyter notebook

#grey image
#imgae_grey=cv2.cvtColor(read_image1,cv2.COLOR_BGR2GRAY)
#cv2.imshow('image_grey',imgae_grey)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#hsv
#imgae_hsv=cv2.cvtColor(read_image1,cv2.COLOR_BGR2HSV)
#cv2.imshow('image_grey',imgae_hsv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

image2_hsv=cv2.cvtColor(read_image1,cv2.COLOR_BGR2HSV)
print(image2_hsv.shape)

#change brightness
def change_brightness(read_image1, add_val):
    image2_hsv=cv2.cvtColor(read_image1,cv2.COLOR_BGR2HSV)
    hue,sat,val=cv2.split(image2_hsv)
    print(val)
    print(val+add_val)
    new_val=val.astype(np.int64)
    new_value2=new_val+add_val
    print(new_value2)

    new_value2[new_value2>255]=255
    new_value2_int8=new_value2.astype(np.uint8)

    new_value2_hsv=cv2.merge([hue,sat,new_value2_int8])
    new_value2_bgr=cv2.cvtColor(new_value2_hsv,cv2.COLOR_HSV2BGR)
    return new_value2_bgr

new_value2_hsv=cv2.merge([hue,sat,new_value2_int8])
new_value2_bgr=cv2.cvtColor(new_value2_hsv,cv2.COLOR_HSV2BGR)
change_brightness(read_image1,500)

cv2.imshow('image', new_value2_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

