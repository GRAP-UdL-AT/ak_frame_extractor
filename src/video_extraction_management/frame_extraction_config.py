"""
Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:
  This file contains config used in frame extraction

Usage:
    BASE_DIR = os.path.abspath('.')
    path_extractor_config_file = os.path.join(BASE_DIR, 'conf', 'frames_extractor.conf')
    frames_extractor_config_obj = FramesManagerConfig(path_extractor_config_file)

"""

import logging
import configparser
import os


class FramesManagerConfig:
    BASE_DIR = os.path.abspath('')
    f_config_name = os.path.join(BASE_DIR, 'conf', 'frames_extractor.conf')
    path_video_input = os.path.join(BASE_DIR, 'recorded_video')
    path_images_output = os.path.join(BASE_DIR, 'exported_images')
    path_mesh_output = os.path.join(BASE_DIR, 'cloud_points')
    # todo: 15/02/2022 check this is temporal
    path_annotations_output = os.path.join(BASE_DIR, 'annotations')

    # used in file names
    rgb_data_filename = 'C'
    depth_data_filename = 'D'
    ir_data_filename = 'I'
    file_img_extension = '.png'
    file_mat_extension = '.mat'
    file_mesh_extension = '.xyz'
    file_csv_extension = '.csv'

    def __init__(self, file_config=None):
        logging.debug('%s - Constructor', type(self).__name__)
        if file_config is None:
            logging.debug('Load default settings!')
            # todo. add checking for other operating systems
            self.set_default()
        else:
            logging.debug('%s - Load settings from file', type(self).__name__)
            if os.path.isfile(file_config):
                self.f_config_name = file_config
                self.read_config()
            else:
                logging.debug('%s - Load default settings, file not found!', type(self).__name__)
                self.set_default()

    def set_default(self):
        self.rgb_data_filename = 'C'
        self.depth_data_filename = 'D'
        self.ir_data_filename = 'I'
        self.file_img_extension = '.png'
        self.file_mat_extension = '.mat'
        self.file_mesh_extension = '.xyz'

    def read_config(self):
        """
        Read config from file frames_extractor.conf
        :return:
        """
        f_config = configparser.ConfigParser()
        f_config.read(self.f_config_name)
        self.path_video_input = f_config['DEFAULT']['path_video_input']
        self.path_images_output = f_config['DEFAULT']['path_images_output']
        self.path_mesh_output = f_config['DEFAULT']['path_mesh_output']
        self.rgb_data_filename = f_config['DEFAULT']['rgb_data_filename']
        self.depth_data_filename = f_config['DEFAULT']['depth_data_filename']
        self.ir_data_filename = f_config['DEFAULT']['ir_data_filename']
        self.file_img_extension = '.' + f_config['DEFAULT']['file_img_extension']
        self.file_mat_extension = '.' + f_config['DEFAULT']['file_mat_extension']
        self.file_mesh_extension = '.' + f_config['DEFAULT']['file_mesh_extension']

    def __del__(self):
        logging.debug('%s - Finalize', type(self).__name__)
