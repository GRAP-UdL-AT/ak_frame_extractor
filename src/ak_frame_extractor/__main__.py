"""
Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor

* PAgFRUIT http://www.pagfruit.udl.cat/en/
* GRAP http://www.grap.udl.cat/

Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda
Date: November 2021
Description:
    User interface that contains functions related to extracting video data from the Azure Kinect camera.

Use:
    python ak_frame_extractor.py

"""
from os.path import expanduser
from helpers.helper_filesystem import *
from gui_frame_ext.gui_frame_ext_console import GUIFrameExtractorConsole2
from gui_frame_ext.gui_frame_ext_config import GUIFrameExtractorConfig2

from dataset_management.dataset_config import DatasetConfig
from video_extraction_management.frame_extraction_config import FramesManagerConfig



if __name__ == '__main__':
    BASE_DIR = os.path.abspath('.')
    ui_path_config_file = os.path.join(BASE_DIR, 'conf', 'ui_frames_extractor.conf')
    path_extractor_config_file = os.path.join(BASE_DIR, 'conf', 'frames_extractor.conf')
    user_path = expanduser("~")
    base_path = os.path.join(user_path)
    dataset_name = 'KA_Story_RGB_IR_DEPTH_dataset'  # by default  # todo: add here an automatic data generation
    dataset_manager_config_obj = DatasetConfig(base_path, dataset_name)
    frames_extractor_config = FramesManagerConfig(path_extractor_config_file)

    user_path = expanduser("~")
    current_main_path_str = __file__
    package_path = os.path.dirname(os.path.normpath(current_main_path_str))
    package_path_config_files = os.path.join(package_path, 'conf')
    path_user_config_files = os.path.join(BASE_DIR, 'conf')

    print('BASE_DIR->', BASE_DIR)
    print('user_path->', user_path)
    print('saved_str', current_main_path_str)
    print('package_path', package_path)
    print('path_user_config_files->', path_user_config_files)

    # if directory doen't exist, then create
    if os.path.exists(path_user_config_files):
        print('Directory exist!!!', path_user_config_files)
    else:
        print('Directory doesnt exist!!!', path_user_config_files)
        print('Creating directory ', path_user_config_files)
        os.mkdir(path_user_config_files)
        copy_folder(package_path_config_files, path_user_config_files)

    # -------------------------
    ui_frame_extractor_config = GUIFrameExtractorConfig2(ui_path_config_file)
    app = GUIFrameExtractorConsole2(ui_frame_extractor_config, dataset_manager_config_obj, frames_extractor_config)
    app.mainloop()
    # -------------------------