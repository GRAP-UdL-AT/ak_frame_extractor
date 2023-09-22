# Packaging data
https://test.pypi.org/project/ak-frame-extractor/
https://pypi.org/project/ak-video-analyser/
https://packaging.python.org/en/latest/tutorials/packaging-projects/

```
py -m twine upload --repository testpypi dist/
```

## Preparing packages
```
py -m pip install --upgrade build
py -m build
```

## Testing package and upload packages

## Testing Pypi.org
```

py -m pip install --upgrade twine
twine upload --repository testpypi ./dist/*
```

## Final repo Pypi.org
```
twine upload ./dist/* --verbose
```

URL: https://test.pypi.org/project/ak-frame-extractor/



## Solving dependencies conflicts

```
pip install -i https://test.pypi.org/simple/ ak-frame-extractor
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple ak-frame-extractor
```

# TODO:
A list of tasks to include in future implementations.

22/09/2023
Refactoring dataset_management
Refactoring frame extraction
Create a renewed test cases list
Verify all the test cases
Verify error messages.
Add check for Matroska video file
Add check for dataset folder
Add get Matroska file properties.
Enable/ disable point cloud generation if the video is not BGRA
Update automatically data for offset from video file
Update version from config.
Check installer for Windows 10
Check configuration files, load data in objects.
Fix windows data size

Tab 03, check dataset folder struct, indicates to the user the creatino of dataset.
Get automatically annotation CSV files.
Add user case to migrate only files, without datset. Translate .CSV to .xml DIRECTOY
Add command line to make it scriptable.
Convert folders to struc without preprocessed/, manage this.
Check struc i n.CSV, launch error
Check structure in .XML, laun error

## User manual tasks
Modify user manual
Add new figures.
Add new videos.

