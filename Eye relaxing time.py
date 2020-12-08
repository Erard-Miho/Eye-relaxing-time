import time
import cv2
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
W, H = screensize

img = cv2.imread('photo.jpg')
windowname = 'Eye Relaxing Time'

height, width, depth = img.shape

scaleWidth = float(W)/float(width)
scaleHeight = float(H)/float(height)
if scaleHeight>scaleWidth:
    imgScale = scaleWidth
else:
    imgScale = scaleHeight

newX, newY = img.shape[1]*imgScale, img.shape[0]*imgScale

newImg = cv2.resize(img, (int(newX), int(newY)))

while True:
    time.sleep(1200)
    cv2.namedWindow(windowname)
   
    cv2.imshow(windowname,newImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
   

   
    
    
    
