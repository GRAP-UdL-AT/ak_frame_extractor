@ echo off
REM Project: AK_FRAEX Azure Kinect Frame Extractor https://github.com/GRAP-UdL-AT/ak_frame_extractor
REM
REM  * PAgFRUIT http://www.pagfruit.udl.cat/en/
REM  * GRAP http://www.grap.udl.cat/
REM
REM  Author: Juan Carlos Miranda. https://github.com/juancarlosmiranda

SET APPLICATION_FOLDER_MAIN=ak_frame_extractor
SET APPLICATION_FOLDER_OUT=ak_frame_extractor_f
SET APPLICATION_PATH=%~dp0

SET CONF_NAME=*.conf
SET PAHT_FOLDER_RELATIVE_CONF=src\%APPLICATION_FOLDER_MAIN%\conf\
SET PATH_CONF_FILE=%APPLICATION_PATH%%PAHT_FOLDER_RELATIVE_CONF%%CONF_NAME%
SET DESTINATION_FOLDER_RELATIVE_CONF=dist\%APPLICATION_FOLDER_OUT%\conf
SET DESTINATION_FOLDER_ABSOLUTE_CONF=%APPLICATION_PATH%%DESTINATION_FOLDER_RELATIVE_CONF%


SET ASSETS_NAME=*.png
SET PAHT_FOLDER_RELATIVE_ASSETS=src\gui_frame_ext\assets\
SET PATH_ASSETS_FILE=%APPLICATION_PATH%%PAHT_FOLDER_RELATIVE_ASSETS%%ASSETS_NAME%
SET DESTINATION_FOLDER_RELATIVE_ASSETS=dist\%APPLICATION_FOLDER_OUT%\gui_frame_ext\assets\
SET DESTINATION_FOLDER_ABSOLUTE_ASSETS=%APPLICATION_PATH%%DESTINATION_FOLDER_RELATIVE_ASSETS%



ECHO %APPLICATION_PATH%
ECHO %PATH_CONF_FILE%
ECHO %DESTINATION_FOLDER_ABSOLUTE_CONF%

ECHO %PATH_ASSETS_FILE%
ECHO %DESTINATION_FOLDER_ABSOLUTE_ASSETS%


REM uncomment the following line if you need to generate again __main__.spec
REM pyi-makespec --paths=%APPLICATION_PATH%src\my_app_name --paths=%APPLICATION_PATH%src\gui_frame_ext --paths=%APPLICATION_PATH%src\helpers %APPLICATION_PATH%src\my_app_name\__main__.py
pyinstaller win_exe_conf/__main__.spec ./src/ka_frame_extractor/__main__.py -y


REM copy .conf files to executable
MKDIR %DESTINATION_FOLDER_ABSOLUTE_CONF%
COPY %PATH_CONF_FILE_CONF% %DESTINATION_FOLDER_ABSOLUTE_CONF%

REM copy icons files
MKDIR %DESTINATION_FOLDER_ABSOLUTE_ASSETS%
COPY %PATH_ASSETS_FILE% %DESTINATION_FOLDER_ABSOLUTE_ASSETS%

cd dist
del ak_frame_extractor_f.zip
"C:\Program Files\7-Zip\7z.exe" a -tzip ak_frame_extractor_f
cd ..