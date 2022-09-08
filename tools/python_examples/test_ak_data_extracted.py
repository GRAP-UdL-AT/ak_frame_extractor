"""
Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: September 2022
Description:

Segmentation using depth information and thresholds
===================================================
This example shows how to load data extracted from videos in .mkv format
using KA_FRAME_EXTRACTOR and its subsequent use in Python's scripts as
.mat files.
Having given frames (RGB and depth data) extracted from video files, it
is filtered by depth threshold value to obtain an RGB fruit image.


Use:
 test_ak_data_extracted.py

"""

import os
import numpy as np
import scipy.stats as stats
import cv2
import scipy.io as sio
from pathlib import Path


def main_data_extraction():
    # setting environment
    home_user = str(Path.home()) # POINT TO "..user folder"
    dataset_root_folder = os.path.join(home_user, 'development', 'ak_frame_extractor', 'data')
    script_path = os.path.join(home_user, 'development', 'ak_frame_extractor', 'tools', 'python_examples')

    # input data examples
    test_images_path = os.path.join(dataset_root_folder)
    test_depth_path = os.path.join(dataset_root_folder)

    # output data
    output_images_path = os.path.join(script_path, 'output_threshold_depth')

    # data names: images and DEPTH
    image_base_name = '20210927_114012_k_r2_e_000_150_138_2_0'
    rgb_image_name = image_base_name + '_C.png'

    depth_image_name = image_base_name + '_D.mat'
    depth_data_path = os.path.join(test_depth_path, depth_image_name)

    # images names for mask 1
    image_segmented_mask_name_2_1 = rgb_image_name + '_mask1.jpg'
    output_segmented_mask_path = os.path.join(output_images_path, image_segmented_mask_name_2_1)

    # load RGB image
    rgb_data_path = os.path.join(test_images_path, rgb_image_name)
    rgb_data = cv2.imread(rgb_data_path)

    # load DEPTH
    depth_mat_data = sio.loadmat(depth_data_path)  # load from file
    depth_data = depth_mat_data['transformed_depth']

    # configure thresholds and getting masks
    threshold_distance = 1400
    temporal_depth_filter = depth_data > 0  # exclude all zero values from matrix

    temporal_depth_selected = depth_data[temporal_depth_filter]  # to get statistics descriptive
    temporal_depth_selected_02 = temporal_depth_selected[temporal_depth_selected < threshold_distance]

    # get descriptive statistics
    mean_depth = np.mean(temporal_depth_selected_02)
    mode_depth = stats.mode(temporal_depth_selected, axis=None)[0][0]
    min_depth = np.min(temporal_depth_selected)
    max_depth = np.max(temporal_depth_selected)

    ones_bit_mask = (temporal_depth_filter == True).astype('int')  # mat data converted from bollean to integer
    depth_mask_1 = np.array(ones_bit_mask * 255, dtype = np.uint8)  # convert ones to img data

    # segmentation with mask 1 single threshold
    rgb_data_segmented_1 = cv2.bitwise_and(rgb_data, rgb_data, mask=depth_mask_1)

    # report results
    print('REPORT-->')
    print(f'mean_depth= {mean_depth}')
    print(f'mean_depth= {mode_depth}')
    print(f'min_depth= {min_depth}')
    print(f'max_depth= {max_depth}')

    # Figures
    cv2.imshow('Original RGB Image', rgb_data)
    cv2.imshow('RGB single threshold', rgb_data_segmented_1)
    cv2.imshow('Mask ones', depth_mask_1)
    cv2.waitKey()

    # save output results
    cv2.imwrite(output_segmented_mask_path, rgb_data_segmented_1)

    pass

if __name__ == '__main__':
    """
    # TODO:  
    """
    """
    Demo dataset structure

    DEMO_dataset \
    | --- \ preprocessed_data
        | --- \ images
        | --- \ annotations
        | --- \ square_annotations1
    """
    main_data_extraction()
    pass
