% ------------------------------------------------------------------------
%Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor
%
%* PAgFRUIT http://www.pagfruit.udl.cat/en/
%* GRAP http://www.grap.udl.cat/
%
%Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
% Date: April 2020
%Description:
%
% ------------------------------------------------------------------------
% Segmentation using depth information and thresholds
% ===================================================
% This example shows how to load data extracted from videos in .mkv format 
% using AK_FRAME_EXTRACTOR and its subsequent use in MATLABs scripts as
% .mat files.
% Having given frames (RGB and depth data) extracted from video files, it 
% is filtered by depth threshold value to obtain an RGB fruit image.
%% setting environment
clc; close all; clear all;
home_user=fullfile('C:','Users', 'Usuari')  % POINT TO "..user root" folder
dataset_root_folder = fullfile(home_user, 'development', 'ak_frame_extractor', 'data')
script_path=fullfile(home_user,'development', 'ak_frame_extractor', 'tools','matlab_examples')

% input data examples
test_images_path=fullfile(dataset_root_folder);
path_test_depth=fullfile(dataset_root_folder);

% output data
output_images_path=fullfile(script_path,'output_threshold_depth');

% data names: images and DEPTH
image_base_name='20210927_114012_k_r2_e_000_150_138_2_0';
rgb_image_name=strcat(image_base_name,'_C.png');

depth_image_name=strcat(image_base_name,'_D.mat');
image_heatmap_orig=strcat(depth_image_name,'_h_orig.jpg');

% images names for mask 1
image_segmented_mask_name_1=strcat(rgb_image_name,'_mask1.jpg');
image_heatmap_name_2_1=strcat(depth_image_name,'_h_2_1.jpg');

% images names for mask 2
image_segmented_mask_name_2_2=strcat(rgb_image_name,'_mask2.jpg');
image_name_heatmap_2_2=strcat(depth_image_name,'_h_2_2.jpg');


%% load RGB image
rgb_data_path=fullfile(test_images_path, rgb_image_name);
rgb_data=imread(rgb_data_path);

%% load DEPTH
load(fullfile(path_test_depth, depth_image_name));
depth_data=transformed_depth; % load from file
% -----------------------

%% configure thresholds and getting masks
threshold_distance=1400;
depth_mask_1=depth_data(:,:)>threshold_distance; % This is a good solution

t1=1200; t2=1400;
depth_mask_2=(depth_data(:,:) >= t1 ) & (depth_data(:,:) <= t2);

%% segmentation with mask 1 single threshold
rgb_data_segmented_1(:,:,1)=immultiply(rgb_data(:,:,1),depth_mask_1);
rgb_data_segmented_1(:,:,2)=immultiply(rgb_data(:,:,2),depth_mask_1);
rgb_data_segmented_1(:,:,3)=immultiply(rgb_data(:,:,3),depth_mask_1);


%% segmentation with mask 2 appliying two thresholds at each end
rgb_data_segmented_2(:,:,1)=immultiply(rgb_data(:,:,1),depth_mask_2);
rgb_data_segmented_2(:,:,2)=immultiply(rgb_data(:,:,2),depth_mask_2);
rgb_data_segmented_2(:,:,3)=immultiply(rgb_data(:,:,3),depth_mask_2);


%% Figures
fo_1=figure('Name','Original RGB Image', 'Position', get(0, 'Screensize')); figure(fo_1); imshow(rgb_data); title(['Original RGB Image']);

%% Mask 1
f1_1=figure('Name','RGB single threshold'); figure(f1_1); imshow(rgb_data_segmented_1); title(['RGB single threshold']);
imwrite(rgb_data_segmented_1, fullfile(output_images_path, image_segmented_mask_name_1), 'png');


