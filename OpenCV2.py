import cv2
image=cv2.imread('images/Image1.jpeg')
print(image)
print(image.shape)
print(image.dtype)

image_grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow('image',image_grey)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#sobel filter
sobel_x=cv2.Sobel(image_grey,ddepth=cv2.CV_64F,dx=1,dy=0)
sobel_y=cv2.Sobel(image_grey,ddepth=cv2.CV_64F,dx=0,dy=1)
sobel_xy=cv2.Sobel(image_grey,ddepth=cv2.CV_64F,dx=1,dy=1)
cv2.imshow('image',sobel_xy)
cv2.waitKey(0)
cv2.destroyAllWindows()