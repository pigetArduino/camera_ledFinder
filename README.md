# camera_ledFinder
Detect led with a webcam using opencv2    
Each images is analysed on a spectrum of colors (Red/Green/Blue) in HSV 
![Webcam image with led highlighted by colored circle](https://github.com/pigetArduino/camera_ledFinder/raw/master/doc/camere_ledFinder_app.png)

# Usage
Download repo and click on dist/camera_ledFinder/camera_ledFinder.exe    

# Compilation
You need 
* miniconda (Python 3.5): http://conda.pydata.org/miniconda.html
* opencv 2 
* pyinstaller (dev version) : https://github.com/pyinstaller/pyinstaller

## Opencv 2
Opencv2 need miniconda to be easily installed
* Type in a command line (WINDOWS+CMD)
```
conda install opencv2
```

## Pyinstaller
* Download pyinstaller on github  : https://github.com/pyinstaller/pyinstaller
* Go to the folder of pyinstaller and type:
```
python setup.py install
```


Source
* http://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
* http://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html
* https://github.com/jlengrand/image_processing/blob/master/LedDetector/leddetector/led_highilighter.py
* http://stackoverflow.com/questions/19189482/color-detection-in-opencv
* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
