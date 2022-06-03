# AK_FRAEX - Azure Kinect Frame Extractor

Python-based GUI tool to extract frames from video files produced with Azure Kinect cameras.

![SOFTWARE_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/ak_frame_extractor_presentation.png?raw=true)

## Contents

1. Pre-requisites.
2. Functionalities.
3. Install and run.
4. Files and folder description.
5. Development tools, environment, build executables.

## 1. Pre-requisites

* Azure Kinect DK camera connected to the computer. Specifications can be seen in
  the [manufacturer site](https://docs.microsoft.com/es-es/azure/kinect-dk/hardware-specification).
* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [pyk4a library](https://pypi.org/project/pyk4a/) installed. If the operating system is Windows, follow
  this [steps](https://github.com/etiennedub/pyk4a/). You can find test basic examples with
  pyk4a [here](https://github.com/etiennedub/pyk4a/tree/master/example).
* In Ubuntu 20.04, we provide a script to install the camera drivers following the instructions
  in [azure_kinect_notes](https://github.com/juancarlosmiranda/azure_kinect_notes).

## 2. Functionalities

The functionalities of the software are briefly described. Supplementary material can be
found in [USER's Manual](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/USER_MANUAL_ak_frame_extractor_v1.md).

* **[Dataset creation]**  This option creates a hierarchy of metadata. This hierarchy contains sub-folders that will be
  used to store the extracted data.
* **[Data Extraction]** The user can configure the parameters for extracting data frames from videos, such as: output
  folder, number of frames to extract. The extraction can be done from one video or by processing a whole folder in
  batch mode.
* **[Data Migration]**  In this tab, we offer a tool for data migration in object labelling tasks. It is used to convert
  files from .CSV format (generated with [Pychet Labeller](https://github.com/acfr/pychetlabeller))
  to [PASCALVOC](https://roboflow.com/formats/pascal-voc-xml) format.

* Data extracted and 3D cloud points can be retrieved from *"your dataset metadata folder"**.

## 3. Install and run

* [Linux]
  Enter to the folder "ak_frame_extractor/"

Create virtual environment(only first time)

```
./creating_evn_ak_frame_extractor.sh
```

Run script.

```
./ak_frame_extractor_start.sh
```

* [Windows]
  Enter to the folder "ak_frame_extractor/"

Create virtual environment(only first time)

```
TODO_HERE
```

Run script from CMD.

```
./ak_frame_extractor_start.bat
```

## 4.3 Files and folder description

Folder description:

| Folders                    | Description            |
|---------------------------|-------------------------|
| docs/ | Documentation |
| src/ | Source code |
| win_exe_conf/ | Specifications for building .exe files with Pyinstaller.|
| tools/ | Examples of code to use data migrated. We offer scripts in MATLAB, Python, R. |
| data/ | Video files recorded with Azure Kinect. |
| . | . |

Files description:

| Files                    | Description              | OS |
|---------------------------|-------------------------|---|
| activate_env.bat | Activate environments in Windows | WIN |
| clean_files.bat | Clean files under CMD. | WIN |
| ak_sm_recorder_main.bat | Executing main script | WIN |
| build_pip.bat | Build PIP package to distribution | WIN |
| build_win.bat | Build .EXE for distribution | WIN |
| creating_env_ak_frame_extractor.sh | Automatically creates Python environments | Linux |
| ak_frame_extractor_start.sh | Executing main script | Linux |
| /src/ak_frame_extractor/__main__.py | Main function used in package compilation | Supported by Python |
| /ak_frame_extractor_main.py | Python main function | Supported by Python |
| setup.cfg | Package configuration PIP| Supported by Python |
| pyproject.toml | Package description pip| Supported by Python |

## 5. Development tools, environment, build executables

Some development tools are needed with this package, listed below:

* [Pyinstaller](https://pyinstaller.org).
* [Opencv](https://opencv.org/).
* [Curses for Python](https://docs.python.org/3/howto/curses.html) ```pip install windows-curses```.
* [7zip](https://7ziphelp.com/).

### 5.1 Notes for developers

You can use the __main__.py for execute as first time in src/ak_frame_extractor/_ _ main _ _.py Configure the path of
the project, if you use Pycharm, put your folder root like this:
![ak_sm_recorder](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/img/configuration_pycharm.png?raw=true)

### 5.2 Creating virtual environment Linux

```
python3 -m venv ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements_linux.txt
```

### 5.3 Creating virtual environment  Windows

```
%userprofile%"\AppData\Local\Programs\Python\Python38\python.exe" -m venv ./venv
venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements_windows.txt
```

** If there are some problems in Windows, follow [this](https://github.com/etiennedub/pyk4a/) **

```
pip install pyk4a --no-use-pep517 --global-option=build_ext --global-option="-IC:\Program Files\Azure Kinect SDK v1.4.1\sdk\include" --global-option="-LC:\Program Files\Azure Kinect SDK v1.4.1\sdk\windows-desktop\amd64\release\lib"
```

## 5.4 Building PIP package

We are working to offer Pypi support for this package. At this time this software can be built by scripts automatically.

### 5.4.1 Build packages

```
py -m pip install --upgrade build
build_pip.bat
```

### 5.4.2 Download PIP package

```
pip install package.whl
```

### 5.4.3 Run ak_frame_extractor

```
python -m ak_frame_extractor.py
```

## 5.4 Building .EXE for Windows 10

```
build_win.bat
```

After the execution of the script, a new folder will be generated inside the project **"/dist"**. You can copy **
ak_frame_extracted_f/** or a compressed file **"ak_frame_Extractor_f.zip"** to distribute.

### 5.6 Package distribution format

Explain about packages distribution.

| Package type | Package |  Url |  Description | 
|--------------|---------|------|------| 
| Windows      | .EXE    | .EXE | Executables are stored under build/ | 
| Linux        | .deb    | .deb | NOT IMPLEMENTED YET| 
| PIP          | .whl    | .whl | PIP packages are stored in build/ |

## Authorship

This project is contributed by [GRAP-UdL-AT](http://www.grap.udl.cat/en/index.html). Please contact authors to report
bugs juancarlos.miranda@udl.cat

## Citation

If you find this code useful, please consider citing:
[GRAP-UdL-AT/ak_frame_extractor](https://github.com/GRAP-UdL-AT/ak_frame_extractor/).
