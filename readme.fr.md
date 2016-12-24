# camera_ledFinder
[Version originale](https://github.com/pigetArduino/camera_ledFinder)


Détecte des leds à l'aide d'une webcam et de la bibliothèque **opencv2**    
Chaque images renvoyés par la webcam est analysé par rapport à un spectre de colors (Rouge/Blue/Vert brillant) en HSV 
![Image d'une webcam où les leds sont mis en avant à led de cercles colorés](https://github.com/pigetArduino/camera_ledFinder/raw/master/doc/camere_ledFinder_app.png)

# Utilisation
Télécharger le repo et cliquer sur **dist/camera_ledFinder/camera_ledFinder.exe**    

# Compilation
Vous devez avoir ceci
* miniconda (Python 3.5): http://conda.pydata.org/miniconda.html
* opencv 2 
* pyinstaller (dev version) : https://github.com/pyinstaller/pyinstaller

## Opencv 2
Opencv2 peut être facilement installé grâce à miniconda
* Tapez dans la ligne de commande (WINDOWS+CMD)
```
conda install opencv2
```

## Pyinstaller
* Télécharger pyinstaller sur github  : https://github.com/pyinstaller/pyinstaller
* Aller dans le dossier de pyinstaller et tapez:
```
python setup.py install
```


Source
* http://www.pyimagesearch.com/2016/02/15/determining-object-color-with-opencv/
* http://docs.opencv.org/3.1.0/d4/d73/tutorial_py_contours_begin.html
* https://github.com/jlengrand/image_processing/blob/master/LedDetector/leddetector/led_highilighter.py
* http://stackoverflow.com/questions/19189482/color-detection-in-opencv
* http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html
