# README AK Frame Extractor
Tool for extracting frames from video files produced with Azure Kinect cameras. 

* [GRAP-UdL-AT/ak_frame_extractor](https://github.com/GRAP-UdL-AT/ak_frame_extractor)

## Contents
* [Installing with virtual environments](https://github.com/GRAP-UdL-AT/ak_frame_extractor)
* [Installing with PIP package](https://github.com/GRAP-UdL-AT/ak_frame_extractor)
* [Notes for developers](https://github.com/GRAP-UdL-AT/ak_frame_extractor)

Before to install this software, and specially Python library pyk4a, it is necessary get installed the sensor at operating system level. For this, follow
instructions to set camera and sensors [azure_kinect_notes](https://github.com/juancarlosmiranda/azure_kinect_notes) 
After that, follow the steps according to your operating system.

## Installing with virtual environments
### Installing Linux (TODO)
Install packages in Ubuntu 20.04
```
sudo apt install python3-tk
```
Create virtual environment.
```
python3 -m venv ./ak_frame_extractor-venv
source ./ak_frame_extractor-venv/bin/activate
pip install -r requirements_linux.txt
```

![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/img/screen_linux.png?raw=true)


### Installing in Windows 10
From command line CMD
```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv ./venv
size_estimation-venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_win.txt
```

![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/img/screen_win.png?raw=true)

### Basic requirements
This software need the following packages:
```
pip install windows-curses
pip install pyk4a
pip install path
pip install opencv-python
```

### Run ak_frame_extractor
Don't forget to activate your preferred virtual environment.
```
python ak_frame_extractor.py
```

## Installing with PIP package
### Build packages
```
py -m pip install --upgrade build
build_pip.bat
```
### Download PIP package
```
pip install package.whl
```

### Run ak_frame_extractor
```
python -m ak_frame_extractor.py
```

## Notes for developers
You can use the __main__.py for execute as first time in src/ak_frame_extractor/_ _ main _ _.py

Configure the path of the project, if you use Pycharm, put your folder root like this:
![alt text](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/img/configuration_pycharm.png?raw=true)


## Authorship
This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html).

Please contact authors to report bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[GRAP-UdL-AT/ak_frame_extractor](https://github.com/GRAP-UdL-AT/ak_frame_extractor/).
