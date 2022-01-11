# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 18:16:08 2021

@author: mluerig
"""

import phenopype as pp
import os

os.chdir(r"D:\workspace\git-repos\phenopype\phenopype-quickstart")


#%% 1. "low-throughput"

## (i) start
image = pp.load_image("stickle1.jpg")

## (ii) preprocessing
mask = pp.preprocessing.create_mask(image, tool="polygon", label="mask1")
img_blur = pp.preprocessing.blur(image, kernel_size=9)

## (iii) segmentation 
img_bin = pp.segmentation.threshold(img_blur, method="adaptive", blocksize=99, constant=5, channel="red", annotations=mask)
contours = pp.segmentation.detect_contour(img_bin, retrieval="ext", min_area=150)

## (iv) measurement
shapes = pp.measurement.compute_shape_features(contours)

## (iv) visualization
canvas = pp.visualization.select_canvas(image, canvas="raw")
canvas = pp.visualization.draw_contour(image, annotations=contours) 
canvas = pp.visualization.draw_mask(canvas, annotations=mask) 
pp.show_image(canvas)

## (v) export
pp.export.save_annotation(mask, dir_path=".", annotation_id="a")
pp.export.save_annotation(contours, dir_path=".", annotation_id="a")
pp.export.save_canvas(canvas, name="stickle1_res", dir_path=".")

#%% 2. "high-throughput"

## create config-file
pp.load_template(template_path="quickstart-template.yaml", tag="quickstart", image_path="stickle1.jpg", overwrite=True)

## run pype
pp.Pype("stickle1.jpg", name="demo", config_path="stickle1_pype_config_quickstart.yaml")



