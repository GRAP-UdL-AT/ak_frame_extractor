# AK_FRAEX - Azure Kinect Frame Extractor

Python-based GUI tool to extract frames from video files produced with Azure Kinect cameras. Visit the project site
at [https://pypi.org/project/ak-frame-extractor/](https://pypi.org/project/ak-frame-extractor/)

![SOFTWARE_PRESENTATION](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/ak_frame_extractor_presentation.png?raw=true)

## Contents

1. Pre-requisites.
2. Functionalities.
3. Install and run.
4. Files and folder description.
5. Development tools, environment, build executables.

## 1. Pre-requisites

* [SDK Azure Kinect](https://docs.microsoft.com/es-es/azure/kinect-dk/set-up-azure-kinect-dk) installed.
* [pyk4a library](https://pypi.org/project/pyk4a/) installed. If the operating system is Windows, follow
  this [steps](https://github.com/etiennedub/pyk4a/). You can find test basic examples with
  pyk4a [here](https://github.com/etiennedub/pyk4a/tree/master/example).
* In Ubuntu 20.04, we provide a script to install the camera drivers following the instructions
  in [azure_kinect_notes](https://github.com/juancarlosmiranda/azure_kinect_notes).
* Videos recorded with the Azure Kinect camera, optional video samples are available at [AK_FRAEX - Azure Kinect Frame Extractor demo videos](https://doi.org/10.5281/zenodo.6968103)


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

### 3.1 PIP quick install package

Create your Python virtual environment.

```
python3 -m venv ./ak_frame_extractor_venv
source ./ak_frame_extractor_venv/bin/activate
pip install --upgrade pip

pip install python -m ak-frame-extractor
python -m ak_frame_extractor
```

### 3.2 Install and run virtual environments using scripts provided

* [Linux]
  Enter to the folder **"ak_frame_extractor/"**

Create virtual environment(only first time)

```
./creating_env_ak_frame_extractor.sh
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
| [docs/](https://github.com/GRAP-UdL-AT/ak_frame_extractor/tree/main/docs) | Documentation |
| [src/](https://github.com/GRAP-UdL-AT/ak_frame_extractor/tree/main/src) | Source code |
| [win_exe_conf/](https://github.com/GRAP-UdL-AT/ak_frame_extractor/tree/main/win_exe_conf) | Specifications for building .exe files with [Pyinstaller](https://pyinstaller.org)..|
| [tools/](https://github.com/GRAP-UdL-AT/ak_frame_extractor/tree/main/tools) | Examples of code to use data migrated. We offer scripts in MATLAB, Python, R. |
| [data/](https://github.com/GRAP-UdL-AT/ak_frame_extractor/tree/main/data) | Examples of output produced by AK_FRAEX, data extracted from recorded video. |
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
![ak_frame_extractor](https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/img/configuration_pycharm.png?raw=true)

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

```
@article{MIRANDA2022101231,
title = {AKFruitData: A dual software application for Azure Kinect cameras to acquire and extract informative data in yield tests performed in fruit orchard environments},
journal = {SoftwareX},
volume = {20},
pages = {101231},
year = {2022},
issn = {2352-7110},
doi = {https://doi.org/10.1016/j.softx.2022.101231},
url = {https://www.sciencedirect.com/science/article/pii/S2352711022001492},
author = {Juan Carlos Miranda and Jordi Gené-Mola and Jaume Arnó and Eduard Gregorio},
keywords = {RGB-D camera, Data acquisition, Data extraction, Fruit yield trials, Precision fructiculture},
abstract = {The emergence of low-cost 3D sensors, and particularly RGB-D cameras, together with recent advances in artificial intelligence, is currently driving the development of in-field methods for fruit detection, size measurement and yield estimation. However, as the performance of these methods depends on the availability of quality fruit datasets, the development of ad-hoc software to use RGB-D cameras in agricultural environments is essential. The AKFruitData software introduced in this work aims to facilitate use of the Azure Kinect RGB-D camera for testing in field trials. This software presents a dual structure that addresses both the data acquisition and the data creation stages. The acquisition software (AK_ACQS) allows different sensors to be activated simultaneously in addition to the Azure Kinect. Then, the extraction software (AK_FRAEX) allows videos generated with the Azure Kinect camera to be processed to create the datasets, making available colour, depth, IR and point cloud metadata. AKFruitData has been used by the authors to acquire and extract data from apple fruit trees for subsequent fruit yield estimation. Moreover, this software can also be applied to many other areas in the framework of precision agriculture, thus making it a very useful tool for all researchers working in fruit growing.}
}
```

## Acknowledgements

This work is a result of the RTI2018-094222-B-I00 project [(PAgFRUIT)](https://www.pagfruit.udl.cat/en/) granted by MCIN/AEI and by the European Regional
Development Fund (ERDF). This work was also supported by the Secretaria d’Universitats i Recerca del Departament
d’Empresa i Coneixement de la Generalitat de Catalunya under Grant 2017-SGR-646. The Secretariat of Universities and
Research of the Department of Business and Knowledge of the [Generalitat de Catalunya](https://web.gencat.cat) and Fons Social Europeu (FSE) are
also thanked for financing Juan Carlos Miranda’s pre-doctoral fellowship [(2020 FI_B 00586)](https://agaur.gencat.cat/). The work of Jordi Gené-Mola
was supported by the Spanish Ministry of Universities through a Margarita Salas postdoctoral grant funded by the
European Union - NextGenerationEU. The authors would also like to thank the Institut de Recerca i Tecnologia
Agroalimentàries [(IRTA)](https://www.irta.cat/es/) for allowing the use of their experimental fields, and in particular Dr. Luís Asín and Dr. Jaume
Lordán who have contributed to the success of this work.


<img src="https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/logo_PAgFRUIT.png" height="60px" alt="PAgFRUIT Research Project"/>
<img src="https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/logo_udl.png" height="60px" alt="Universitat de Lleida"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/logo_goverment_calonia.png" height="60px" alt="Generalitat de Catalunya"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/logo_min_science.png" height="60px" alt="Ministerio de Ciencia, Innovación y Universidades"/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/logo_UNIO_EUROPEA.png" height="60px" alt="Fons Social Europeu (FSE) "/>
&nbsp;&nbsp;&nbsp;<img src="https://github.com/GRAP-UdL-AT/ak_frame_extractor/blob/main/docs/img/logo_AGAUR.png" height="60px" alt="AGAUR"/>
