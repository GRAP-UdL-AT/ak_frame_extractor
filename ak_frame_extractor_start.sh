#!/bin/bash

# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

# commands definitions
PYTHON_CMD='python3'

# folders names definitions
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# files extensions names
EXT_SCRIPTS_SH='*.sh'
EXT_ZIP='.zip'

# folders names definitions
DEVELOPMENT_PATH='development'
DEVELOPMENT_ENV_PATH='development_env'
COMMON_ENV_PATH='bin/activate'


# software folders names
FRAME_EXTRACTOR_NAME='ak_frame_extractor-main'


# project folders
ROOT_FOLDER_F=$HOME/$DEVELOPMENT_PATH/ #$ROOT_FOLDER_NAME/
FRAME_EXTRACTOR_NAME_F=$ROOT_FOLDER_F$FRAME_EXTRACTOR_NAME/

# environment folders
ENV_NAME='_venv'
ROOT_ENV_F=$HOME/$DEVELOPMENT_ENV_PATH/ #$ROOT_FOLDER_NAME$ENV_NAME/
FRAME_EXTRACTOR_NAME_ENV_F=$ROOT_ENV_F$FRAME_EXTRACTOR_NAME$ENV_NAME/

# activating environments
source $FRAME_EXTRACTOR_NAME_ENV_F$COMMON_ENV_PATH

python ak_frame_extractor_main.py
deactivate
