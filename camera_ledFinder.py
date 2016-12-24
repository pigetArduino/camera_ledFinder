'''
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
'''

# http://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
# http://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html
# https://github.com/jlengrand/image_processing/blob/master/LedDetector/leddetector/led_highilighter.py
# http://stackoverflow.com/questions/19189482/color-detection-in-opencv
# http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html


import cv2
import numpy
import time
import webcolors
import colorsys


min_threshold = 200
max_threshold = 255

def show_webcam(mirror=False):
  cam = cv2.VideoCapture(0)
  while True:
    ret_val, img = cam.read()
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    low_red = numpy.array([0,min_threshold,min_threshold])
    high_red = numpy.array([20,max_threshold,max_threshold])

    low_green = numpy.array([50,min_threshold,min_threshold])
    high_green = numpy.array([100,max_threshold,max_threshold])

    low_blue = numpy.array([100,min_threshold,min_threshold])
    high_blue = numpy.array([150,max_threshold,max_threshold])

    mask_red = cv2.inRange(hsv,low_red,high_red)
    mask_green = cv2.inRange(hsv,low_green,high_green)
    mask_blue = cv2.inRange(hsv,low_blue,high_blue)


    im2, contours_red, hierarchy = cv2.findContours(mask_red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    im2, contours_green, hierarchy = cv2.findContours(mask_green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    im2, contours_blue, hierarchy = cv2.findContours(mask_blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(img, contours_green, -1, (0,255,0), 50)
    cv2.drawContours(img, contours_red, -1, (0,0,255), 50)
    cv2.drawContours(img, contours_blue, -1, (255,0,0), 50)



    
    cv2.imshow('image',img)
    
    
    if cv2.waitKey(1) == 27: 
        break  # esc to quit
  cv2.destroyAllWindows()



def position(event,x,y,flags,param):
    print(x,y)
    time.sleep(1)

def main():
    cv2.namedWindow('image')
    #cv2.setMouseCallback('image',position)
    show_webcam(mirror=True)

if __name__ == '__main__':
    main()