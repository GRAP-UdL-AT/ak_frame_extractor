# ------------------------------------------------------------------------
# Project: Fruit Size Estimation
# Author: https://github.com/juancarlosmiranda/
# Date: May 2022
#  ------------------------------------------------------------------------
#  Simple infrarred and depth data
#  ===================================================
#  This example shows how to load infrarred and depth data extracted from 
#  videos in .mkv format using AK_FRAME_EXTRACTOR and its subsequent use in 
#  MATLABs scripts as .mat files.
#  setting environment

#install.packages("here")
#install.packages("R.matlab")

library(here)
library(R.matlab)
here()

home_user='C:/Users/Usuari/development/ak_frame_extractor'
path_script=home_user

# input data examples
path_test_images=paste(path_script,'/data/',sep="")
path_test_depth=paste(path_script,'/data/',sep="");
path_test_ir=paste(path_script,'/data/',sep="");

# output data
path_output_images=paste(path_script,'tools','matlab_examples/output_threshold_depth/');

# data names: images and DEPTH
image_base_name='20210927_114012_k_r2_e_000_150_138_2_0'
rgb_image_name=paste(image_base_name,'_C.png',sep="")
depth_image_name=paste(image_base_name,'_D.mat',sep="")
ir_image_name=paste(image_base_name,'_I.mat',sep="")

# load DEPTH images to test
depth_image_name_m <- readMat(paste(path_test_depth, depth_image_name, sep=""))
head(depth_image_name_m$transformed.depth)

# load IR images to test
ir_image_name_m <- readMat(paste(path_test_ir, ir_image_name, sep=""))
head(ir_image_name_m$transformed_ir)

# -----------------------
depth_data=depth_image_name_m$transformed.depth #load from file .mat
ir_data=ir_image_name_m$transformed_ir #load from file .mat
# -----------------------

