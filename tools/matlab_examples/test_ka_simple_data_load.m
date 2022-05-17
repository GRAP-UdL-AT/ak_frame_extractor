% ------------------------------------------------------------------------
% Project: Fruit Size Estimation
% Author: https://github.com/juancarlosmiranda/
% Date: April 2020
% ------------------------------------------------------------------------
% Simple infrarred and depth data
% ===================================================
% This example shows how to load infrarred and depth data extracted from 
% videos in .mkv format using KA_FRAME_EXTRACTOR and its subsequent use in 
% MATLABs scripts as .mat files.
%% setting environment
clc; close all; clear all;
home_user=pwd  % POINT TO "..\ka_frame_extractor\" folder
path_script=fullfile(home_user)

% input data examples
path_test_images=fullfile(path_script,'\data\');
path_test_depth=fullfile(path_script,'\data\');
path_test_ir=fullfile(path_script,'\data\');

% output data
path_output_images=fullfile(path_script,'tools','matlab_examples/output_threshold_depth/');

% data names: images and DEPTH
image_base_name='20210927_114012_k_r2_e_000_150_138_2_0';
rgb_image_name=strcat(image_base_name,'_C.png');
depth_image_name=strcat(image_base_name,'_D.mat');
ir_image_name=strcat(image_base_name,'_I.mat');

%% load DEPTH and RGB images to test
load(fullfile(path_test_depth, depth_image_name));
load(fullfile(path_test_ir, ir_image_name));
IRGBPath=fullfile(path_test_images, rgb_image_name);

% -----------------------
rgb_data=imread(IRGBPath);
depth_data=transformed_depth; % load from file .mat
ir_data=transformed_ir; % load from file .mat
% -----------------------

% Visualise data
heatmap_fig_1 = figure('WindowState','maximized');
heatmap_handle_ir = heatmap(heatmap_fig_1, depth_data,...
    'Colormap',[0 0 0.52;0 0 0.56;0 0 0.6;0 0 0.64;0 0 0.68;0 0 0.72;0 0 0.76;0 0 0.8;0 0 0.84;0 0 0.88;0 0 0.92;0 0 0.96;0 0 1;0 0.04 1;0 0.08 1;0 0.12 1;0 0.16 1;0 0.2 1;0 0.24 1;0 0.28 1;0 0.32 1;0 0.36 1;0 0.4 1;0 0.44 1;0 0.48 1;0 0.52 1;0 0.56 1;0 0.6 1;0 0.64 1;0 0.68 1;0 0.72 1;0 0.76 1;0 0.8 1;0 0.84 1;0 0.88 1;0 0.92 1;0 0.96 1;0 1 1;0.04 1 0.96;0.08 1 0.92;0.12 1 0.88;0.16 1 0.84;0.2 1 0.8;0.24 1 0.76;0.28 1 0.72;0.32 1 0.68;0.36 1 0.64;0.4 1 0.6;0.44 1 0.56;0.48 1 0.52;0.52 1 0.48;0.56 1 0.44;0.6 1 0.4;0.64 1 0.36;0.68 1 0.32;0.72 1 0.28;0.76 1 0.24;0.8 1 0.2;0.84 1 0.16;0.88 1 0.12;0.92 1 0.08;0.96 1 0.04;1 1 0;1 0.96 0;1 0.92 0;1 0.88 0;1 0.84 0;1 0.8 0;1 0.76 0;1 0.72 0;1 0.68 0;1 0.64 0;1 0.6 0;1 0.56 0;1 0.52 0;1 0.48 0;1 0.44 0;1 0.4 0;1 0.36 0;1 0.32 0;1 0.28 0;1 0.24 0;1 0.2 0;1 0.16 0;1 0.12 0;1 0.08 0;1 0.04 0;1 0 0;0.96 0 0;0.92 0 0;0.88 0 0;0.84 0 0;0.8 0 0;0.76 0 0;0.72 0 0;0.68 0 0;0.64 0 0;0.6 0 0;0.56 0 0;0.52 0 0],...
    'YLimits',{'205','875'},...
    'XLimits',{'400','1591'},...
    'Title','DEPTH data');

heatmap_fig_2 = figure('WindowState','maximized');
heatmap_handle_ir = heatmap(heatmap_fig_2, ir_data,...
    'Colormap',[0 0 0.52;0 0 0.56;0 0 0.6;0 0 0.64;0 0 0.68;0 0 0.72;0 0 0.76;0 0 0.8;0 0 0.84;0 0 0.88;0 0 0.92;0 0 0.96;0 0 1;0 0.04 1;0 0.08 1;0 0.12 1;0 0.16 1;0 0.2 1;0 0.24 1;0 0.28 1;0 0.32 1;0 0.36 1;0 0.4 1;0 0.44 1;0 0.48 1;0 0.52 1;0 0.56 1;0 0.6 1;0 0.64 1;0 0.68 1;0 0.72 1;0 0.76 1;0 0.8 1;0 0.84 1;0 0.88 1;0 0.92 1;0 0.96 1;0 1 1;0.04 1 0.96;0.08 1 0.92;0.12 1 0.88;0.16 1 0.84;0.2 1 0.8;0.24 1 0.76;0.28 1 0.72;0.32 1 0.68;0.36 1 0.64;0.4 1 0.6;0.44 1 0.56;0.48 1 0.52;0.52 1 0.48;0.56 1 0.44;0.6 1 0.4;0.64 1 0.36;0.68 1 0.32;0.72 1 0.28;0.76 1 0.24;0.8 1 0.2;0.84 1 0.16;0.88 1 0.12;0.92 1 0.08;0.96 1 0.04;1 1 0;1 0.96 0;1 0.92 0;1 0.88 0;1 0.84 0;1 0.8 0;1 0.76 0;1 0.72 0;1 0.68 0;1 0.64 0;1 0.6 0;1 0.56 0;1 0.52 0;1 0.48 0;1 0.44 0;1 0.4 0;1 0.36 0;1 0.32 0;1 0.28 0;1 0.24 0;1 0.2 0;1 0.16 0;1 0.12 0;1 0.08 0;1 0.04 0;1 0 0;0.96 0 0;0.92 0 0;0.88 0 0;0.84 0 0;0.8 0 0;0.76 0 0;0.72 0 0;0.68 0 0;0.64 0 0;0.6 0 0;0.56 0 0;0.52 0 0],...
    'YLimits',{'205','875'},...
    'XLimits',{'400','1591'},...
    'Title','IR data');