#!/bin/bash
# Project: AK_ACQS Azure Kinect Acquisition System https://github.com/GRAP-UdL-AT/ak_acquisition_system
#
# * PAgFRUIT http://www.pagfruit.udl.cat/en/
# * GRAP http://www.grap.udl.cat/
#
# Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

set -e

FILENAME_ZIP='ak_frame_extractor-main.zip'
REQUERIMENTS_LINUX='requirements_linux.txt'

# commands definitions
PYTHON_CMD='python3'
UNZIP_CMD=`which unzip`
MKDIR_CMD='mkdir -p'
CHMOD_CMD='chmod 755'
PIP_INSTALL_CMD='pip install'
PIP_UPDATE_CMD='pip install --upgrade pip'

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

# creating environments automatically
$PYTHON_CMD -m venv $FRAME_EXTRACTOR_NAME_ENV_F
source $FRAME_EXTRACTOR_NAME_ENV_F$COMMON_ENV_PATH
$PIP_UPDATE_CMD
$PIP_INSTALL_CMD -r $FRAME_EXTRACTOR_NAME_F$REQUERIMENTS_LINUX
deactivate

