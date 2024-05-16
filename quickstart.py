# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:16:08 2021

@author: mluerig
"""

## Also see https://www.phenopype.org/docs/tutorials/tutorial_3/

import phenopype as pp
import os

## change after downloading - e.g.:
## os.chdir(r"C:\Users\mluerig\Downloads\phenopype-quickstart-main")
os.chdir(r"D:\git-repos\phenopype\phenopype-quickstart")

#%% 1. Python mode 

## (i) load image
image = pp.load_image("stickle1.jpg")

## (ii) preprocessing
mask = pp.preprocessing.create_mask(image, tool="polygon", label="mask1")
img_blur = pp.preprocessing.blur(image, kernel_size=9)

## (iii) segmentation 
img_bin = pp.segmentation.threshold(img_blur, method="adaptive", blocksize=99, constant=5, annotations=mask)
contours = pp.segmentation.detect_contour(img_bin, retrieval="ext", min_area=150)

## (iv) measurement
shapes = pp.measurement.compute_shape_features(contours)

## (iv) visualization
canvas = pp.visualization.select_canvas(image, canvas="raw")
canvas = pp.visualization.draw_contour(image, annotations=contours) 
canvas = pp.visualization.draw_mask(canvas, annotations=mask) 
pp.show_image(canvas)

## (v) export
save_dir = os.getcwd()
pp.export.save_annotation(mask, dir_path=save_dir)
pp.export.save_annotation(contours, dir_path=save_dir)
pp.export.save_canvas(canvas, file_name="stickle1_canvas", dir_path=save_dir)

## (vi) export 2 (optional)
## name annotations with the same tag prefix so that they can be loaded by the Pype-class
pp.export.save_annotation(mask, dir_path=save_dir, file_name ="stickle1_annotations_quickstart.json")
pp.export.save_annotation(contours, dir_path=save_dir, file_name ="stickle1_annotations_quickstart.json")


#%% 2. Interactive mode 

## run Pype class using the loaded config file
## note that your previously drawn masks are loaded - delete the annotations json file to redo them
pp.Pype(image_path="stickle1.jpg", tag="quickstart", config_path="quickstart-template.yaml")


