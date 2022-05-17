# README Code samples and tools
We provide examples in MATLAB to show the use of data exported using KA Frame Extractor.
Data and images can be uploaded with common routines in MATLAB.


## Example 1) Load .mat file exported from a dataset created.
```
test_ka_simple_data_load.m
```
This example shows how to load infrared and depth data extracted from videos in .mkv format using KA_FRAME_EXTRACTOR and its subsequent use in MATLABs scripts as .mat files.


DEPTH data ![alt text](https://github.com/GRAP-UdL-AT/ka_frame_extractor/blob/main/tools/img/DEPTH_data_exported.png?raw=true)


IR data ![alt text](https://github.com/GRAP-UdL-AT/ka_frame_extractor/blob/main/tools/img/IR_data_exported.png?raw=true)


## Example 2) Load .mat file exported from a dataset created.
```
test_ka_data_extracted.m.m
```

This example shows how to load data extracted from videos in .mkv format using KA_FRAME_EXTRACTOR and its subsequent use in MATLABs scripts as .mat files. Having given frames (RGB and depth data) extracted from video files, it is filtered by depth threshold value to obtain a segmented RGB fruit image.

Original Image ![alt text](https://github.com/GRAP-UdL-AT/ka_frame_extractor/blob/main/tools/img/20210927_114012_k_r2_e_000_150_138_2_0_C.png?raw=true)

Segmented image ![alt text](https://github.com/GRAP-UdL-AT/ka_frame_extractor/blob/main/tools/img/20210927_114012_k_r2_e_000_150_138_2_0_C.png_mask1.jpg?raw=true)